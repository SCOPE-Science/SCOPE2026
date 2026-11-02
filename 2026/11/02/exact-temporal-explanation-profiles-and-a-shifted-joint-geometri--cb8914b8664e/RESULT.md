# Exact temporal-explanation profiles and a shifted joint geometric law for Until

## Finding

For the standard finite-trace Until formula \(\varphi=p\,\mathsf U\,q\) at the first position of a length-\(n\ge1\) trace, all subset-minimal abductive and contrastive explanations (AXps and CXps) have explicit trace-dependent normal forms given below. If the \(2n\) propositional observations are independent fair bits, let \(A_n\) and \(C_n\) denote the respective **numbers** of AXps and CXps. Then their full conditional joint laws converge in total variation, and for integers \(a,c\),

\[
\lim_{n\to\infty}\Pr(A_n=a,C_n=c\mid\varphi)
=\begin{cases}\displaystyle\frac{\binom{c-1}{a-1}}{2\,4^{c-1}},&c\ge1,\ 1\le a\le c,\\0,&\text{otherwise,}\end{cases}
\]
\[
\lim_{n\to\infty}\Pr(A_n=a,C_n=c\mid\neg\varphi)
=\begin{cases}\displaystyle\frac{\binom{c-2}{a-1}}{2\,4^{c-2}},&c\ge2,\ 1\le a<c,\\0,&\text{otherwise.}\end{cases}
\]

Thus the limiting joint distribution conditioned on violation is obtained by increasing the number of CXps by exactly one from the limiting distribution conditioned on satisfaction, with no change in the number of AXps. In either outcome \(\Pr(A=a)=2/3^a\) for \(a\ge1\). The limiting conditional bivariate probability-generating functions are

\[
\frac{2st}{4-(1+s)t}\quad\text{and}\quad\frac{2st^2}{4-(1+s)t}
\]

for satisfaction and violation respectively, on \(0\le s,t\le1\). In both cases \(\mathbb E A=3/2\) and \(\operatorname{Cov}(A,C)=1\); the conditional mean numbers of CXps converge to \(2\) and \(3\).

The theorem also gives exact finite-length conditional laws, not just an asymptotic statement.

## Assumptions and scope

The trace is \(\pi=((p_0,q_0),\ldots,(p_{n-1},q_{n-1}))\in\{0,1\}^{2n}\), with \(n\ge1\). The strong finite-trace Until semantics is

\[
F_n(\pi)=1\quad\Longleftrightarrow\quad
\exists j\in\{0,\ldots,n-1\}:q_j=1\ \text{and}\ p_i=1\ (0\le i<j).
\]

The truth value at position zero is considered. For a given trace, a subset of its signed time-indexed literals is an AXp if fixing it forces the observed outcome under **every** completion of the same length and no proper subset does. A subset is a CXp if allowing exactly those positions to change (holding all other observations fixed) permits the opposite outcome and no proper subset does. These are subset-minimal, not minimum-cardinality, explanations. For counting we choose each of the \(2n\) bits independently Bernoulli \((1/2)\); all \(4^n\) length-\(n\) traces are equally likely. This is a fixed-length, fair-bit theorem only.

To describe sets of explanations write \(P_i\) and \(Q_j\) for the positive literals when the corresponding observations equal one, and \(\bar P_i\), \(\bar Q_j\) for the negative literals when they equal zero. Each displayed set of literals is an **entire** AXp or CXp, not an element of an explanation.

## Proof

**1. Complete positive profiles.** Let \(J=\{j:q_j=1,\ p_i=1\text{ for }i<j\}\). On a satisfying trace \(J\ne\varnothing\); set \(L=\max J\). Exactly the following are the AXps:

\[
\mathcal A^+(\pi)=\big\{\{Q_j\}\cup\{P_i:0\le i<j\}:j\in J\big\}.
\]

The CXps are precisely

\[
\mathcal C^+(\pi)=
\big\{\{Q_j:j\in J\}\big\}
\cup\big\{\{P_i\}\cup\{Q_j:j\in J,\ j\le i\}:0\le i<L\big\}.
\]

In particular \(A_n=|J|\) and \(C_n=L+1\). To prove completeness, expand the Until formula into the monotone disjunctive normal form \(F_n=\bigvee_{j<n}(q_j\wedge\bigwedge_{i<j}p_i)\). Its inclusion-minimal positive implicants are exactly these disjuncts: each contains a unique \(q_j\), and no proper subset guarantees an Until witness. The consistent prime implicants on a positive trace are indexed by \(J\), proving the AXp list. CXps are the minimal hitting sets of these implicants: either hit all using their \(Q_j\)'s, or choose an earliest \(P_i\) and take precisely the \(Q_j\)'s with \(j\le i\). A second \(P_i\), or a \(P_i\) beyond \(L-1\), is redundant. The construction and irredundancy establish the displayed list.

**2. Complete negative profiles.** Put \(z=\min\{j:q_j=1\}\), with \(z=n\) when no such index exists, and \(I=\{i<z:p_i=0\}\). If \(z<n\), the trace is negative exactly when \(I\ne\varnothing\). Then its AXps and CXps are

\[
\mathcal A^-(\pi)=\big\{\{\bar P_i\}\cup\{\bar Q_j:0\le j\le i\}:i\in I\big\},
\]
\[
\mathcal C^-(\pi)=
\big\{\{\bar P_i:i\in I\}\big\}
\cup\big\{\{\bar Q_j\}\cup\{\bar P_i:i\in I,\ i<j\}:0\le j\le\max I\big\}.
\]

Consequently \(A_n=|I|\), \(C_n=\max I+2\). If instead \(z=n\), then

\[
\mathcal A^-(\pi)=
\big\{\{\bar Q_j:0\le j<n\}\big\}
\cup\big\{\{\bar P_i\}\cup\{\bar Q_j:0\le j\le i\}:0\le i<n-1,\ p_i=0\big\},
\]
\[
\mathcal C^-(\pi)=
\big\{\{\bar Q_j\}\cup\{\bar P_i:0\le i<j,\ p_i=0\}:0\le j<n\big\}.
\]

So \(A_n=1+|\{i<n-1:p_i=0\}|\) and \(C_n=n\) when every \(q_j\) is false. Completeness follows by taking the minimal hitting sets of the positive terms in Step 1. To force violation, either fix all \(q_j\)'s to zero or fix one \(p_i\) to zero together with all earlier (and same-time) \(q_j\)'s to zero. When \(i=n-1\), the second option is subsumed by the all-\(q\) option. The remaining negative AXps are incomparable, and their minimal transversals give exactly the two displayed negative-CXp cases. This reasoning covers the boundary \(n=1\).

**3. Exact finite joint counts.** The probability of satisfaction obeys the recursion \(r_0=0\), \(r_n=1/2+r_{n-1}/4\), hence

\[
\Pr(F_n=1)=\frac23(1-4^{-n}).
\]

For \(0\le l<n\), the probability of the event \(\{F_n=1,L=l\}\) is

\[
\alpha_{n,l}=2^{-l-1}\left(\frac23+\frac{4^{-(n-l-1)}}3\right).
\]

On this event, the earlier \(q\)-bits remain independent fair bits, so \(A_n=1+\operatorname{Bin}(l,1/2)\) and \(C_n=l+1\). Thus, for integers \(1\le a\le l+1\),

\[
\Pr(F_n=1,A_n=a,C_n=l+1)
=\alpha_{n,l}\binom l{a-1}2^{-l}.
\]

For a negative trace with at least one \(q_j=1\), let \(l=\max I\); here \(0\le l\le n-2\). The joint mass of this event is

\[
\beta_{n,l}=\frac{2^{-l-1}}3\left(1-4^{-(n-l-1)}\right).
\]

The earlier \(p\)-bits remain independent fair bits, hence

\[
\Pr(F_n=0,z<n,A_n=a,C_n=l+2)
=\beta_{n,l}\binom l{a-1}2^{-l}
\]

for \(1\le a\le l+1\). Finally, the event \(z=n\) has mass \(2^{-n}\); independently \(A_n=1+\operatorname{Bin}(n-1,1/2)\) and \(C_n=n\), so its joint mass at \((a,n)\) is \(2^{-n}\binom{n-1}{a-1}2^{-(n-1)}\). These formulas completely determine the finite joint distribution and its overlap of contributions at equal \((a,c)\).

For \(\alpha_{n,l}\), the bits through \(l\) must establish a witness at \(l\); either \(p_l=0\), or \(p_l=1\) and the remaining suffix contains no new witness. Since a suffix of length \(d\) contains no witness with probability \((1+2\cdot4^{-d})/3\), the displayed formula follows. For \(\beta_{n,l}\), require \(q_j=0\) for \(j\le l\), \(p_l=0\), then allow a geometric-length run of pairs \((p=1,q=0)\) before the first \(q=1\); summing that geometric series gives the formula. The free earlier bits yield the binomial factors.

**4. Joint limit and convergence mode.** For each fixed \(l\ge0\), \(\alpha_{n,l}\to(2/3)2^{-l-1}\), \(\beta_{n,l}\to(1/3)2^{-l-1}\), while \(\Pr(F_n=1)\to2/3\) and \(\Pr(F_n=0)\to1/3\). Hence conditional on either outcome the respective index \(l\) has limiting geometric law \(\Pr(l)=2^{-l-1}\), and conditional on that index \(A=1+\operatorname{Bin}(l,1/2)\). The positive CXp count is \(l+1\), the negative CXp count is \(l+2\). These facts give both displayed joint mass functions.

For total-variation convergence, couple all finite traces to one infinite i.i.d. sequence. The first false \(p\) and first true \(q\) occur at almost surely finite indices. Once a finite prefix contains both indices, the truth value and both explanation counts for the prefix no longer change with extension. The probability that at least one has not occurred in the first \(n\) positions is at most \(2^{1-n}\). Conditioning on either outcome (whose probabilities tend to positive constants) preserves convergence in total variation. Summing the geometric-binomial mixture gives the two rational generating functions, the common marginal \(2/3^a\), and the stated moments.

## Verification

The independent exhaustive checker `checker.py` enumerates all \(4^n\) traces for lengths \(1\le n\le4\) and, for each, all possible locked/unlocked subsets, comparing independently evaluated subset minimality against both structural lists. It then checks every exact finite joint-count identity for \(1\le n\le7\) using rational arithmetic and exhaustive trace enumeration. Executing `python3 checker.py` produces `ALL_CHECKS_OK`. The exhaustive computations are finite cross-checks; the preceding proof establishes all lengths and the limit.

## Relationship to prior work

Cuartas Granada, Ignatiev and Stuckey (February 2026) develop general explanation-enumeration methods for finite-automata decisions; the Until predicate is recognized by a finite automaton, so its explanation problem is a concrete instance of their framework. The present claim is the specialized **complete trace-level normal form and exact finite/asymptotic joint counting distribution** for this basic temporal automaton, not the general definitions or algorithms. Fionda, Ielo and Ricca (October 2026) subsequently defined equivalent finite-trace AXps/CXps directly through locked and unlocked observations and established classifier equivalence; their work supplies a later semantic comparison, not the motivating source date. Ferrère, Maler and Ničković (2015) develop temporal implicants, including inductive diagnostics for infinite-time LTL and MTL. Their inspected material does not state these finite-trace pair-count identities. Classical prime-implicant/minimal-transversal duality and geometric waiting-time formulas are used and not claimed as new.

## Limitations

The input model is a uniformly random fixed-length trace with two independently fair propositions; neither biased/correlated traces nor nested Until formulas are covered. The limiting statement concerns **numbers** of explanations, not their lengths. A general earlier theorem for prime implicants of nested monotone Boolean functions might imply part of the classification; no claim of exhaustive literature coverage or independent priority certification is made. The relevant 2025 Meng--Alrajeh paper was identified bibliographically but its full text was unavailable for direct comparison. The proof has not undergone independent mathematical review.

## References

- J. Cuartas Granada, A. Ignatiev and P. J. Stuckey, *A Formal Framework for the Explanation of Finite Automata Decisions*, arXiv:2602.13351, first submitted 2026-02-12. https://arxiv.org/abs/2602.13351
- V. Fionda, A. Ielo and F. Ricca, *Formal Explanations for Linear Temporal Logic over Finite Traces*, arXiv:2610.35169, first submitted 2026-10-26 (later comparative source). https://arxiv.org/abs/2610.35169
- T. Ferrère, O. Maler and D. Ničković, *Trace Diagnostics Using Temporal Implicants*, ATVA 2015, pp. 241--258, DOI:10.1007/978-3-319-24953-7_20. Author manuscript: https://thomasferrere.com/TraceDiagnosticsUsingTemporalImplicants.pdf
- H. Meng and D. Alrajeh, *Causal Detection in Linear Temporal Counterexamples*, FSE Companion 2025, DOI:10.1145/3696630.3731617 (bibliographic comparison only).
