# Sharp cyclic one-step preimage runner-up for elementary Rule 126

## Finding

Let \(F_n\) be Fibonacci numbers with \(F_0=0\), \(F_1=1\), and \(L_n=F_{n-1}+F_{n+1}\) the Lucas numbers for \(n\ge1\). Let \(T_n\) be the synchronous elementary cellular automaton Rule 126 on \(n\) indexed cyclic binary sites, and define the one-step fiber count \(d_n(y)=|\{x\in\{0,1\}^n:T_n(x)=y\}|\).

For **every integer \(n\ge7\)**, \(1^n\) is the unique maximum-fiber output, with
\[
d_n(1^n)=\begin{cases}L_n+2,&3\mid n,\\L_n-1,&3\nmid n.\end{cases}
\]
The **exact second-largest** fiber, taken over all outputs other than \(1^n\), is
\[
\max_{y\ne1^n}d_n(y)=F_{n-2}+\tau_{n-1},\qquad
\tau_j=\begin{cases}1,&j\equiv0\pmod3,\\0,&j\equiv1\pmod3,\\-1,&j\equiv2\pmod3.\end{cases}
\]
Equality in the second statement holds **exactly** for the \(n\) indexed outputs having a single zero and \(n-1\) ones (all rotations of \(0 1^{n-1}\)). These outputs are distinct for \(n\ge7\).

A stronger exact fiber identity used to prove the extremal claims is the following. If \(y\ne1^n\) has \(k\ge1\) zero sites and \(a_1,\ldots,a_k\) are the successive cyclic numbers of ones between those zero sites, then, with the backward extension \(F_{-1}=1\),
\[
d_n(y)=\prod_{i=1}^k F_{a_i-1}+\prod_{i=1}^k\tau_{a_i}.
\]
This identity is valid for every integer \(n\ge1\), including adjacent zeros and the all-zero word. It is a structural counting identity; the claimed new extremal classification concerns the periodic-ring runner-up.

## Assumptions and scope

Sites are indexed modulo \(n\); input and output words are not quotiented by rotation or complementation. Rule 126 has local Boolean output \(f(a,b,c)=0\) exactly when \(a=b=c\), and output \(1\) otherwise. Each input site is updated simultaneously once, with periodic boundary conditions; there is no temporal iteration beyond that single update.

All multiplicities are ordinary counts of distinct indexed initial configurations. The second-largest fiber is defined by excluding the unique global maximizer \(1^n\), not by imposing a positive-fiber condition; since the displayed runner-up is positive, the interpretation coincides with the maximum over other reachable outputs. Results at ring lengths below seven are not part of the extremal assertion.

## Proof

**1. Closed-walk representation.** Index the two-letter de Bruijn states in order \(00,01,10,11\). The transition \(ab\to bc\) has label \(f(a,b,c)\). Write \(P\) for the adjacency matrix of transitions labeled zero, and \(B\) for those labeled one:
\[
P=\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix},\qquad
B=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0\end{pmatrix}.
\]
By following the ordered input pairs around the ring, each indexed input \(x\) mapping to an indexed output \(y\) corresponds bijectively to one closed walk of length \(n\) with specified edge labels. Hence \(d_n(y)=\operatorname{tr}(B_{y_0}\cdots B_{y_{n-1}})\), where \(B_0=P\), \(B_1=B\). This remains valid even at \(n=1,2\), because the closed walk enforces the cyclic identifications.

**2. The zero-gap product.** For \(y\ne1^n\), rotate cyclically to begin at a zero. Its matrix product is cyclically trace-equivalent to \(PB^{a_1}PB^{a_2}\cdots PB^{a_k}\). Restricting to the \(00\) and \(11\) states reduces the trace to the product of \(2\times2\) matrices \(C_a=(B^a)_{\{00,11\},\{00,11\}}\). Global bit complementation commutes with \(B\), so \(C_a=\bigl(\begin{smallmatrix}u_a&v_a\\v_a&u_a\end{smallmatrix}\bigr)\); its eigenvalues are \(s_a=u_a+v_a\) and \(t_a=u_a-v_a\).

On complement-symmetric vectors, the action of \(B\) is \(E=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\). On complement-antisymmetric vectors, it is \(O=\bigl(\begin{smallmatrix}0&1\\-1&-1\end{smallmatrix}\bigr)\). The corresponding top-left entries of \(E^a\) and \(O^a\) are respectively \(s_a\) and \(t_a\). Since \(E^2=E+I\) and \(O^2=-O-I\), and both sequences begin with values \((1,0)\) at \(a=0,1\), we obtain \(s_a=F_{a-1}\) using \(F_{-1}=1\), and \(t_a=\tau_a\) with period three. Simultaneous diagonalization of every \(C_a\) gives
\[
d_n(y)=\operatorname{tr}\Bigl(\prod_i C_{a_i}\Bigr)=\prod_i F_{a_i-1}+\prod_i\tau_{a_i}.
\]

**3. The homogeneous-one fiber.** In the same complement-symmetric and antisymmetric decomposition, \(B\) is similar to the direct sum \(E\oplus O\). The characteristic polynomials are \(z^2-z-1\) and \(z^2+z+1\). Consequently \(\operatorname{tr}(E^n)=L_n\) and \(\operatorname{tr}(O^n)=2\) for \(3\mid n\), otherwise \(-1\). Thus \(d_n(1^n)=L_n+(2\text{ if }3\mid n\text{ else }-1)\).

**4. Strict runner-up bound.** For an output with exactly one zero, its sole gap is \(a_1=n-1\), so the product formula gives \(d_n(y)=F_{n-2}+\tau_{n-1}\). For outputs with at least two zeros, if any gap equals one, both factors in the product formula vanish. Otherwise each gap is zero or at least two. Let \(r\) denote the number of positive gaps and \(S\) their sum; since there are at least two zeros, \(S\le n-2\). The identity
\[
F_{p+q-1}=F_pF_q+F_{p-1}F_{q-1}\qquad(p,q\ge1)
\]
proves by induction that for \(r\ge1\), \(\prod_{a_i\ge2}F_{a_i-1}\le F_{S-2r+1}\le F_{n-3}\). Zero gaps contribute the factor \(F_{-1}=1\). If \(r=0\), the Fibonacci product equals one, also at most \(F_{n-3}\) for \(n\ge7\). As \(|\prod_i\tau_{a_i}|\le1\), every output containing at least two zeros has
\[
d_n(y)\le F_{n-3}+1.
\]
For \(n=7\), \(F_5+\tau_6=6>F_4+1=4\). For every \(n\ge8\),
\[
F_{n-2}+\tau_{n-1}-(F_{n-3}+1)=F_{n-4}+\tau_{n-1}-1\ge F_{n-4}-2>0.
\]
Hence exactly the \(n\) single-zero outputs are runners-up. Finally \(L_n-1>F_{n-2}+1\) for \(n\ge7\), so the all-one fiber is strictly larger and the global maximizer is unique. All comparisons are exact and valid without asymptotic assumptions.

## Verification

Run `python3 verify.py` with Python 3. The program enumerates **every indexed initial configuration and every indexed output** for each ring length \(1\le n\le16\), checks the exact product formula, and verifies the stated extremal values and equality cases for \(7\le n\le16\). Independently, it reconstructs the de Bruijn labeled adjacency matrices and checks every closed-walk trace formula through length ten. The expected terminal marker is `VERIFY_OK`. This finite replay is a check of the formulas, **not** a substitute for the all-length proof above.

For comparison, the counts at lengths \(n=7,8,9,10,11,12\) are respectively global maxima \(28,46,78,122,198,324\), runner-up values \(6,8,12,22,34,54\), with precisely \(n\) runners-up in every case.

## Relationship to prior work

Jen's 1987 and 1989 papers establish general preimage enumeration recurrences for one-dimensional cellular automata. Her 1989 paper explicitly gives a **finite linear-block** Rule-126 Fibonacci formula and observes that the all-one **linear block** has maximum preimage count; this known homogeneous phenomenon is not claimed as original here. The finite periodic-ring boundary identification changes the count and introduces the two eigenmodes, including the period-three correction. The exact second-largest cyclic-ring fiber and the complete one-zero equality class do not follow as stated from the published linear-block maximization. They require an all-length comparison over every competing cyclic zero-gap pattern.

Martínez, Adamatzky, Seck-Tuoh-Mora and Alonso-Sanz examine Rule 126, its de Bruijn diagrams, and memory dynamics, but the inspected relevant material does not establish the exact runner-up cyclic fiber. Fukś studies multistep preimage sequences and their recurrences on infinite lattices, not this fixed one-step cyclic ranking. The general transfer-matrix framework is standard and is not presented as newly discovered. An exact description of the cyclic **image set** would determine whether a fiber is empty, but would not determine positive fiber multiplicities. Results for other elementary rules also do not transfer merely by renaming the local rule.

## Limitations

The extremal statement is restricted to \(n\ge7\), single-step Rule 126, and periodic **indexed** binary rings. The general product formula includes smaller rings but does not itself establish multistep preimage distributions. It provides no claim about random nonuniform initial configurations, other elementary rules, or all possible near-maximal ranking levels. Generic matrix enumeration methods and linear-block preimage formulas were previously known; historical priority of this particular cyclic runner-up classification has not been independently audited.

## References

1. Erica Jen, *Scaling of Preimages in Cellular Automata*, Complex Systems 1 (1987), 1045–1062. https://content.wolfram.com/sites/13/2018/02/01-6-2.pdf
2. Erica Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems 3 (1989), 421–456; especially Eq. (4.11) and Section 5.4. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
3. G. J. Martínez, A. Adamatzky, J. C. Seck-Tuoh-Mora, and R. Alonso-Sanz, *How to Make Dull Cellular Automata Complex by Adding Memory: Rule 126 Case Study*, Complexity 15 (2010), 34–49; public arXiv version 1212.0124v1 (2012-12-01). https://arxiv.org/abs/1212.0124
4. H. Fukś, *Sequences of Preimages in Elementary Cellular Automata*, Complex Systems 14 (2002), 29–43; arXiv:1305.6533v1 (2013-05-28). https://arxiv.org/abs/1305.6533
