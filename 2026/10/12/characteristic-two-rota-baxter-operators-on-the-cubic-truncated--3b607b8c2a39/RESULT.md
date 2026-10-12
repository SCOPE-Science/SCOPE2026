# Characteristic-two Rota–Baxter operators on the cubic truncated polynomial algebra

## Finding
Let \(q=2^e\) with \(e\ge1\), and put
\[
A_q=\mathbb F_q[t]/(t^3).
\]
A weight-zero Rota–Baxter operator is an \(\mathbb F_q\)-linear map \(P:A_q\to A_q\) satisfying
\[
P(x)P(y)=P\bigl(P(x)y+xP(y)\bigr)\qquad(x,y\in A_q).
\]
Every such operator is uniquely
\[
P_{a,b}(1)=a t^2,\qquad P_{a,b}(t)=b t^2,\qquad P_{a,b}(t^2)=0
\]
for \((a,b)\in\mathbb F_q^2\). Consequently there are exactly \(q^2\) operators. The zero operator is the unique rank-zero operator, all other \(q^2-1\) operators have rank one, and \(P_{a,b}^2=0\) for every \((a,b)\).

The algebra automorphisms are
\[
\phi_{{u,v}}(t)=ut+vt^2\qquad(u\in\mathbb F_q^\times,\ v\in\mathbb F_q).
\]
Conjugation acts on the parameter plane by
\[
\phi_{{u,v}}P_{{a,b}}\phi_{{u,v}}^{{-1}}=P_{{u^2a,ub}}.
\]
Thus there are exactly \(q+2\) conjugacy classes: the zero class; one class with \(a\ne0,b=0\); one class with \(a=0,b\ne0\); and, when \(ab\ne0\), the \(q-1\) classes indexed by
\[
\rho=\frac{{a}}{{b^2}}\in\mathbb F_q^\times.
\]
Every nonzero orbit has size \(q-1\).

## Assumptions and scope
The coefficient field is an arbitrary finite field of characteristic two. The algebra is the unital cubic truncation \(A_q\); in particular its maximal ideal \((t)\) has nonzero square \((t^2)\). The operator weight is zero. Equivalence in the orbit statement means conjugation by unital \(\mathbb F_q\)-algebra automorphisms. No assertion is made here about nonzero weights or about truncations of degree greater than three.

## Proof
Write
\[
P(1)=a_0+a_1t+a_2t^2,\quad P(t)=b_0+b_1t+b_2t^2,\quad P(t^2)=c_0+c_1t+c_2t^2.
\]
Because the Rota–Baxter defect is bilinear, it is enough to impose the identity on the nine ordered pairs from the basis \(1,t,t^2\).

First use the pair \((t^2,t^2)\). Characteristic two makes the argument on the right equal to zero, while
\[
P(t^2)^2=c_0^2+c_1^2t^2.
\]
A field has no nonzero square-zero scalar, hence \(c_0=c_1=0\). Now the pair \((1,t^2)\) reads
\[
c_2a_0t^2=(a_0+c_2)c_2t^2,
\]
so \(c_2^2=0\) and therefore \(c_2=0\). Thus \(P(t^2)=0\).

For the pair \((t,t)\), again the right-hand argument is \(2tP(t)=0\). Therefore
\[
P(t)^2=b_0^2+b_1^2t^2=0,
\]
which forces \(b_0=b_1=0\). Hence \(P(t)=b_2t^2\). Finally, the pair \((1,1)\) gives \(P(1)^2=0\), so \(a_0=a_1=0\). The remaining basis-pair identities are then automatic. Renaming \(a_2=a\) and \(b_2=b\) proves the classification, count, rank statement, and \(P^2=0\).

Every algebra automorphism must preserve the unique maximal ideal and induce a nonzero scalar on \((t)/(t^2)\), so it has the displayed form \(\phi_{{u,v}}\), and every such map is invertible. Since \(\phi_{{u,v}}(t^2)=u^2t^2\) and
\[
\phi_{{u,v}}^{{-1}}(t)=u^{{-1}}t+vu^{{-3}}t^2
\]
in characteristic two, direct substitution gives \((a,b)\mapsto(u^2a,ub)\). On the mixed locus \(ab\ne0\), the ratio \(a/b^2\) is invariant, and choosing \(u=b^{{-1}}\) sends each pair to the unique representative \((a/b^2,1)\). Squaring is an automorphism of \(\mathbb F_q^\times\), so the two coordinate axes each form one nonzero orbit. The parameter \(v\) acts trivially; hence each nonzero orbit has \(q-1\) elements. This gives \(q+2\) orbits in total.

## Verification
The standalone verifier `artifacts/verify.py` independently enumerates every linear endomorphism of the three-dimensional algebra over \(\mathbb F_2\) and \(\mathbb F_4\), tests the Rota–Baxter identity on all basis pairs, and compares the complete solution set with the theorem. It also computes ranks, constructs all algebra automorphisms in these two fields, recomputes conjugacy orbits, and verifies the invariant \(a/b^2\). As a characteristic boundary check it exhaustively enumerates \(\mathbb F_3\), where the solution count is \(2q^2-q=15\), rather than the characteristic-two value \(q^2\). The recorded run ends with `VERIFY_OK`.

The finite computations are checks, not the proof for arbitrary \(q\); the proof above uses only field axioms and characteristic two.

## Relationship to prior work
Zheng–Guo–Rosenkranz study Rota–Baxter operators on the full polynomial algebra \(k[t]\); their 2014 preprint is the archive anchor and the published article lists primary MSC 16W99. Their monomial and injective classifications do not classify the finite quotient \(A_q\).

Li–Hou–Bai work over \(\mathbb C\) and their three-dimensional table contains the commutative associative algebra labelled C12, which is exactly \(\mathbb C[t]/(t^3)\) after identifying their unit and nilpotent basis. Their table displays two complex parameter families, one involving the coefficient \(2\). This is the strongest same-object prior comparison. Its standing complex-field hypothesis does not cover characteristic two, where those displayed families collapse, nor can it rule out additional modular solutions. The proof above resolves that modular boundary directly and additionally determines the finite-field automorphism-conjugacy classes.

Farooq classifies truncated polynomial algebras of the form \(K[x_1,\ldots,x_n]/\mathfrak m^2\) in characteristic zero. Those algebras have square-zero maximal ideal, whereas \((t)^2=(t^2)\ne0\) in \(A_q\), so that result does not imply this cubic characteristic-two classification.

## Limitations
The theorem is restricted to characteristic two, cubic truncation, and weight zero. It does not claim that the complex C12 table is new, nor does it infer novelty merely from unsuccessful searches. The literature comparison is strongest for the exact complex same-object classification and the recent square-zero truncated-polynomial classification; unindexed positive-characteristic work remains a residual originality risk.

## References
1. S. Zheng, L. Guo, M. Rosenkranz, “Rota–Baxter operators on the polynomial algebra, integration, and averaging operators,” arXiv:1407.5306v1 (2014); Pacific J. Math. 275 (2015), 481–507.
2. X. Li, D. Hou, C. Bai, “Rota-Baxter operators on pre-Lie algebras,” J. Nonlinear Math. Phys. 14 (2007), 269–289, DOI:10.2991/jnmp.2007.14.2.9.
3. A. Farooq, “Rota Baxter Operators on Truncated Polynomial Algebras,” arXiv:2605.15670v1 (2026).
