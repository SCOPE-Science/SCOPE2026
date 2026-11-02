# Exact consistency enumeration for random binary constraints on cycles

## Finding
For every integer \(n\geq 3\), put one independent uniformly sampled binary relation on each edge of the labelled simple cycle \(C_n\), each relation being one of the \(16\) subsets of \(\{0,1\}^2\). A system is *consistent* when some assignment of the \(n\) vertex bits satisfies every edge relation. Its exact consistency probability is
\[
\boxed{q(C_n)=s^n+t^n-4^{-n}-\frac{1}{2\cdot8^n}},\qquad
s=\frac{17+\sqrt{97}}{32},\quad t=\frac{17-\sqrt{97}}{32}.
\]
Equivalently, if \(N_n\) is the number of consistent systems among the \(16^n\) labelled edge-relation systems, then
\[
\boxed{N_n=U_n-4^n-2^{n-1}},\qquad
U_0=2,\quad U_1=17,\quad U_n=17U_{n-1}-48U_{n-2}\quad(n\ge2).
\]
The first counts are \(N_3=2397\), \(N_4=32377\), \(N_5=435537\), \(N_6=5850913\), and \(N_7=78563553\).

This corrects the final term in Horak and Semaev's Conjecture 20 (2026), which proposes \(-8^{1-n}\) instead of \(-1/(2\cdot8^n)\). For every \(n\ge3\), the actual consistency probability exceeds the conjectured expression by exactly \(15/(2\cdot8^n)\). In particular, the direct three-cycle count is \(2397/4096\), whereas that conjectured expression is \(2337/4096\).

## Assumptions and scope
The cycle has distinct vertices \(x_0,\ldots,x_{n-1}\), with edge \(i\) connecting \(x_i\) to \(x_{i+1\bmod n}\). Each of its \(n\) edge functions is independently uniformly selected from the \(16\) Boolean functions on two bits; its allowed relation contains exactly the ordered pairs on which the chosen function evaluates to zero. This is precisely the uniformly random polynomial truth-table model over \(\mathbb F_2\), since each Boolean function has a unique multilinear polynomial representation over \(\mathbb F_2\). A consistent system means existence of at least one simultaneous zero, not uniqueness or an expected number of zeros. Edges and vertices remain labelled; no quotient by rotation, reflection, or truth-table symmetries is taken.

## Proof
**1. Boolean composition.** Encode an allowed binary relation by a \(2\times2\) Boolean matrix with entries \(R_{ij}\in\{0,1\}\). Define the Boolean product by \((R\circ B)_{ij}=\bigvee_{k\in\{0,1\}}(R_{ik}\land B_{kj})\). Its \((i,i)\) entry is one precisely when a length-two walk with the prescribed endpoint bit exists. Consequently, a cyclic edge-relation system is consistent if and only if \(B_0\circ\cdots\circ B_{n-1}\) has a nonzero diagonal entry.

**2. Exact seven-orbit transfer.** Use bit-mask encoding \(R=\sum_{i,j\in\{0,1\}}2^{2i+j}R_{ij}\). Under independent permutations of rows and columns, the sixteen masks split into seven classes with respective smallest representatives
\[
0,\ 1,\ 3,\ 5,\ 6,\ 7,\ 15.
\]
The one-step transition count \(T_{ab}\) is the number of the sixteen uniform second factors \(B\) for which \(R_a\circ B\) lies in class \(b\). It is well-defined on classes: replacing \(R_a\) by \(P R_a Q\) permutes the uniform collection \(QB\), while the output multiplication by \(P\) preserves its class. Enumerating sixteen possible \(B\) for each listed representative gives the following integer transition matrix, in the displayed class order:
\[
T=\begin{pmatrix}
16&0&0&0&0&0&0\\
4&8&4&0&0&0&0\\
1&6&9&0&0&0&0\\
4&0&0&8&0&0&4\\
1&4&2&2&2&4&1\\
1&2&1&4&0&4&4\\
1&0&0&6&0&0&9
\end{pmatrix}.
\]
For a relation \(R\) with \(w\) allowed pairs, exactly \(2^{4-w}\) of the sixteen matrices \(B\) produce a Boolean product \(R\circ B\) having zero diagonal: each one in position \((i,k)\) of \(R\) forbids the distinct entry \(B_{ki}\). Thus the last-factor acceptance vector is
\[
g=(0,8,12,12,12,14,15)^{\mathsf T}.
\]
The identity relation, mask \(9\), is in the fifth class (mask \(6\) represents that class). With \(e_5\) the fifth coordinate vector, the exact count for any \(n\ge1\) is
\[
N_n=e_5^{\mathsf T}T^{n-1}g.
\]
For \(n=1,2\) this merely defines auxiliary relation-product counts; the graph assertion concerns simple cycles with \(n\ge3\).

**3. Exact linear annihilator.** Direct multiplication of the displayed integer matrix and vector establishes
\[
(T-4I)(T-2I)(T^2-17T+48I)g=0.
\]
This is an entrywise integer identity, independently reconstructed in the included verifier. As all factors are polynomials in \(T\), it follows that \(N_n\) obeys the order-four recurrence with characteristic polynomial
\[
(\lambda-4)(\lambda-2)(\lambda^2-17\lambda+48).
\]
The transfer count yields \(N_1=12\), \(N_2=175\), \(N_3=2397\), and \(N_4=32377\). Let \(U_n\) be the Lucas-type recurrence specified in the finding. Its characteristic roots are \((17\pm\sqrt{97})/2\). Therefore \(U_n-4^n-2^{n-1}\) obeys precisely the same order-four recurrence and has those same four initial values (starting at \(n=1\)). Uniqueness of a recurrence solution proves the integer count for every \(n\ge1\). Dividing by \(16^n\) proves the claimed probability formula for all \(n\ge3\), since \(U_n/16^n=s^n+t^n\).

**4. Comparison with the conjectured expression.** The proposed term \(8^{1-n}\) equals \(8/8^n\), but the transfer gives \(1/(2\cdot8^n)\). Their difference is \(15/(2\cdot8^n)\). For \(n=3\), the integer formula gives \(2397/4096\), while direct substitution in Conjecture 20 gives \(2337/4096\); these are distinct. This proves both the corrected formula and a counterexample to the published conjectural formula under its stated uniform random-equation model.

## Verification
Run `python3 verify.py` using Python 3 with no external dependencies. It recomputes every orbit, checks invariance of every transition row across all members of each orbit, verifies the acceptance vector and polynomial-annihilator identity over the integers, and verifies the formula against transfer counts for \(1\le n\le60\). Independently of the transfer construction, it exhaustively enumerates all \(16^3+16^4=69632\) binary-relation systems on the three- and four-cycles, testing all bit assignments. A second independent inclusion-exclusion implementation counts their satisfying systems from the projections of nonempty assignment families. All methods give \(2397\) and \(32377\), respectively. These finite checks are supplementary: the infinite proof is the exact transfer identity and recurrence.

## Relationship to prior work
Horak and Semaev, *Inconsistency Probability of Sparse Equations over F2* (arXiv:2603.24890v1, dated 2026-03-26), Section 4.5, Conjecture 20, introduces the same fixed-cycle, uniformly random two-variable-equation model and proposes the above expression with a different final term. Their results on paths, stars, and forests are not claimed here. The corrected cycle formula is not a deduction from that conjecture, since its value for \(C_3\) is false; it is obtained by an independent relation-composition enumeration. Dovgal, de Panafieu, and Ravelomanana, *Exact enumeration of satisfiable 2-SAT formulae* (arXiv:2108.08067v2), count formulae in models defined by an overall number or probability of CNF clauses, rather than an independent uniformly chosen truth table on each edge of a prescribed simple cycle. A binary relation can be encoded by forbidding assignments with clauses, but their cited unrestricted clause-count results do not directly assert the present fixed-edge relation-system probability.

## Limitations
The result is exact for uniformly independent binary truth tables on the edges of labelled simple cycles \(C_n\) with \(n\ge3\). It does not address biased relations, arbitrary support graphs, repeated edges, constraints involving three or more variables, the distribution of the number of satisfying assignments, or asymptotic complexity of solving instances. Finite checks alone would not prove the formula; the displayed integer-matrix identity supplies the all-\(n\) argument. Historical-priority comparison is limited to retrieved relevant research sources and does not establish global uniqueness.

## References
1. P. Horak and I. Semaev, *Inconsistency Probability of Sparse Equations over F2*, arXiv:2603.24890v1 (first public version dated 2026-03-26), in particular Section 4.5, Conjecture 20. https://arxiv.org/abs/2603.24890
2. S. Dovgal, É. de Panafieu, and V. Ravelomanana, *Exact enumeration of satisfiable 2-SAT formulae*, arXiv:2108.08067v2 (2022), subsequently *Combinatorial Theory* **3** (2023). https://arxiv.org/abs/2108.08067
