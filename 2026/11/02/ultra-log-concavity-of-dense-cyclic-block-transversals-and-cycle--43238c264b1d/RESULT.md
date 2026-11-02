# Ultra-log-concavity of dense cyclic-block transversals and cycle-power domination

## Finding
Let \(q\ge1\) and \(q+1\le n\le2q+1\) be integers. For each \(i\in\mathbb Z/n\mathbb Z\), let \(B_i=\{i,i+1,\ldots,i+q-1\}\), with indices taken cyclically. Let \(h_s(n,q)\) count the \(s\)-element sets meeting every \(B_i\), and let \(h_0(n,q)=0\). Then
\[
H_{n,q}(z)=\sum_{s=0}^n h_s(n,q)z^s=(1+z)^n-1-nz(1+z)^{n-q-1}.
\]
Moreover the normalized sequence \(p_s=h_s(n,q)/\binom ns\), \(0\le s\le n\), is log-concave, including its zero boundaries: \(p_s^2\ge p_{s-1}p_{s+1}\) for every \(1\le s<n\). The positive support is an interval, so the counting sequence is **ultra-log-concave**.

**Graph consequence.** Let \(\ell\ge1\) and \(3\le n\le4\ell+3\). The ordinary domination polynomial of the power \(C_n^\ell\) of the simple cycle is ultra-log-concave. For \(2\ell+2\le n\le4\ell+3\), it has the explicit form
\[
D(C_n^\ell;z)=(1+z)^n-1-nz(1+z)^{n-2\ell-2}.
\]
For \(n\le2\ell+1\), the power is complete and \(D(C_n^\ell;z)=(1+z)^n-1\). This proves a two-parameter dense-power region of Conjecture 1.8 of Galvin and Zhang [1]. For example, \(D(C_{11}^{2};z)=(1+z)^{11}-1-11z(1+z)^5\), with exactly \(55\) three-element dominating sets.

## Assumptions and scope
The cyclic blocks are subsets, not sequences: \(1\le q<n\), and each \(B_i\) has size exactly \(q\). The graph \(C_n\) is the simple cycle for \(n\ge3\); its \(\ell\)-th power joins vertices at graph distance at most \(\ell\). A dominating set meets the closed neighborhood of every vertex. The domination polynomial counts every named vertex subset by size; it is not a generating function for inclusion-minimal dominating sets. Ultra-log-concavity refers to normalization by \(\binom ns\), not ordinary coefficient log-concavity alone. The complete-graph case is included separately.

## Proof
**1. Exact enumeration of cyclic transversals.** Fix a nonempty \(s\)-subset \(S\) of the \(n\)-cycle and list its chosen vertices in cyclic order. It fails to meet some \(q\)-consecutive block exactly when one cyclic gap from a chosen vertex to the next contains at least \(q\) unchosen vertices; equivalently, its step length is at least \(q+1\). The sum of all cyclic step lengths is \(n\). Since \(n\le2q+1\), two gaps of length at least \(q+1\) are impossible. Therefore a nontransversal has a **unique** long gap. Its starting chosen vertex can be selected in \(n\) ways; the next \(q\) vertices must be absent; the other \(s-1\) chosen vertices can be any subset of the remaining \(n-q-1\) positions. There are exactly \(n\binom{n-q-1}{s-1}\) nontransversals of size \(s\), where out-of-range binomial coefficients are zero. Subtracting from \(\binom ns\) and treating the empty set separately proves the polynomial identity. No inclusion-exclusion approximation is being made.

**2. Normalized failure probabilities.** Put \(t=n-q-1\), so \(0\le t\le q\) and \(n=t+q+1\). Set
\[
b_s=\frac{n\binom{t}{s-1}}{\binom ns}=\frac{s\binom{t}{s-1}}{\binom{n-1}{s-1}}
\quad (1\le s\le n),
\]
interpreting \(b_s=0\) for \(s\ge t+2\). Then \(p_0=0\), \(p_1=0\), and \(p_s=1-b_s\) for \(s\ge1\). The first equality is the exact nontransversal probability under uniform sampling of an \(s\)-subset; hence \(0\le b_s\le1\).

Where the ratios are defined, put \(R_s=b_{s+1}/b_s\). For \(1\le s\le t+1\),
\[
R_s=\frac{(s+1)(t-s+1)}{s(n-s)}.
\]
For \(2\le s\le t+1\), direct simplification yields
\[
R_{s-1}-R_s=\frac{(q-t)[s(s-1)+t+1]+(t+1)[(s-1)(s-2)+2t]}{s(s-1)(n-s)(n-s+1)}\ge0.
\]
All displayed factors are nonnegative and the denominators are positive, since \(q\ge t\). Thus \(b_s\) is log-concave on its positive support, including the endpoint where \(b_{t+2}=0\).

For \(3\le s\le t+1\) the same ratios give the second difference
\[
\frac{b_{s-1}-2b_s+b_{s+1}}{b_s}
=\frac{q((s-1)q+s-2t-3)}{s(t+2-s)(n-s)}\ge0,
\]
because \((s-1)q+s-2t-3\ge(s-3)(t+1)\ge0\). Thus the normalized failure probabilities are also convex starting at index three. Combining the two inequalities,
\[
\begin{aligned}
p_s^2-p_{s-1}p_{s+1}
&=(b_{s-1}-2b_s+b_{s+1})
 +(b_s^2-b_{s-1}b_{s+1})\ge0
\end{aligned}
\]
for \(3\le s\le t+1\). At \(s=1,2\), the inequalities follow from \(p_0=p_1=0\). At \(s\ge t+2\), \(p_s=1\) and all neighboring \(p\)-values belong to \([0,1]\), giving the remaining inequalities. When \(t<2\), the middle range is empty and the boundary argument still applies. Finally \(p_2=(q-t)/(n-1)\ge0\); the ratios imply \(p_s>0\) for every \(s\ge3\), so there are no internal zeros. This completes the ultra-log-concavity proof.

**3. Transfer to cycle powers.** For \(n\le2\ell+1\), every pair of vertices of \(C_n\) is at distance at most \(\ell\), so the power is complete. If \(n\ge2\ell+2\), each closed neighborhood in \(C_n^\ell\) consists of exactly \(q=2\ell+1\) consecutive vertices. Hence its dominating sets are precisely the transversals counted above. The condition \(n\le4\ell+3\) is exactly \(n\le2q+1\), so the theorem applies.

## Verification
The accompanying standalone file `verify.py` recomputes the cyclic-block transversal numbers by direct subset enumeration for every admissible \(n\le15\), independently reconstructs graph neighborhoods and dominating sets for each admissible cycle power of order at most \(15\), and checks the normalized log-concavity inequalities with exact integers. It also evaluates the asserted closed forms and inequalities for \(13,040\) additional graph-parameter pairs. Run `python3 verify.py`; the expected output starts with `VERIFY_OK`. The mathematical proof above covers unbounded \(n\) and \(q\); the finite checks are supplementary.

## Relationship to prior work
Galvin and Zhang [1] proved **unimodality** of the domination polynomial for all powers of paths and cycles, and proposed the stronger **ultra-log-concavity** claim as Conjecture 1.8. Their cycle recurrence and complete-graph initial conditions cover coefficients recursively, but do not imply the normalized three-term coefficient inequalities proved here. The range \(n=2\ell+2\) is covered by their explicit polynomial identity; the new assertion is the ultra-log-concavity across the entire two-parameter range \(3\le n\le4\ell+3\), including the noncomplete cases. Omar [2] independently studied normalized domination probabilities and gave criteria for unimodality plus log-concavity for threshold graphs; those results do not establish this cycle-power ultra-log-concavity statement. The underlying transversal interpretation is standard and is not claimed as new.

## Limitations
The unique-long-gap counting argument only applies when \(n\le2q+1\). At \(n=2q+2\) two long gaps can coexist, so neither the displayed polynomial nor its log-concavity proof extends automatically. No claim is made about the remaining powers \(n\ge4\ell+4\), path powers, arbitrary graphs, or independent publication priority. The theorem is supported by an explicit proof and finite consistency tests, but no independent audit is claimed.

## References
[1] D. Galvin and Y. Zhang, *The domination polynomial of powers of paths and cycles*, arXiv:2408.12731, first public preprint 22 August 2024; especially Theorems 1.4--1.5 and Conjecture 1.8. https://arxiv.org/abs/2408.12731

[2] M. Omar, *New Perspectives On The Unimodality Of Domination Polynomials*, arXiv:2601.14494, posted 20 January 2026; sections on normalized domination probabilities and threshold-graph log-concavity. https://arxiv.org/abs/2601.14494
