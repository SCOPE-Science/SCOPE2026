# Theta-modulated cubic suppression of noncentral ideals in free class-two Lie algebras

## Finding
Fix any prime power \(q\ge2\). Let \(V_d=\mathbb F_q^d\), \(d\ge2\), and let \(L_d=V_d\oplus\bigwedge^2V_d\) have bracket \([v+z,w+z']=v\wedge w\). Write \(I_d\) for a uniformly chosen Lie ideal of \(L_d\), and \(N_d=\binom d2\).

Define the two convergent theta series
\[
\Theta_0(q)=\sum_{j\in\mathbb Z}q^{-j^2},\qquad
\Theta_{1/2}(q)=\sum_{j\in\mathbb Z}q^{-(j+1/2)^2}.
\]
For integers \(r\), put \(\Theta_{[r]}(q)=\Theta_0(q)\) if \(r\) is even, and \(\Theta_{1/2}(q)\) otherwise. Let \(M_d=\binom{d-1}{2}\).

**Theorem.** As \(d\to\infty\) with \(q\) fixed,
\[
\boxed{\Pr(I_d\not\subseteq Z(L_d))
=\frac{\Theta_{[M_d+1]}(q)}{(1-q^{-1})\Theta_{[N_d]}(q)}
q^{-d^3/4+d^2-d/2}(1+o(1)).}
\]
Thus the logarithmic exponent is cubic, with a genuinely four-periodic theta prefactor in \(d\bmod 4\). Moreover,
\[
\Pr\bigl(\dim ((I_d+Z(L_d))/Z(L_d))=1\mid I_d\not\subseteq Z(L_d)\bigr)\longrightarrow1.
\]
The theorem concerns the generator-rank limit \(d\to\infty\), not the local index-growth limit at fixed \(d\).

## Assumptions and scope
The field is any finite field of cardinality \(q\), with no characteristic restriction. The bracket on \(L_d\) is alternating, including in characteristic two. For \(d\ge2\), its center is exactly \(Z(L_d)=\bigwedge^2V_d\), of dimension \(N_d\). Ideals are \(\mathbb F_q\)-linear and two-sided in the Lie sense. All probabilities use the uniform distribution over the *finite set of all ideals*, not the uniform distribution over dimensions or over generating sets.

For \(n\ge0\) and \(0\le k\le n\), write \({n\brack k}_q\) for the number of \(k\)-subspaces of \(\mathbb F_q^n\); it is the Gaussian binomial coefficient. The precise finite-field rank-refined identity used in the proof is
\[
\#\{I\lhd L_d:\dim\pi(I)=a\}
={d\brack a}_q\sum_{c=0}^{\binom{d-a}{2}}{\binom{d-a}{2}\brack c}_q q^{ac},\qquad 0\le a\le d,
\]
where \(\pi:L_d\to V_d\) is projection. This finite identity is supporting enumeration; the claimed distinction from existing ideal-zeta work is the sharp uniform-in-\(d\) asymptotic and rare-defect structure above.

## Proof
**1. Classification and exact counting.** Let \(I\) be an ideal and set \(A=\pi(I)\le V_d\), \(W=I\cap\bigwedge^2V_d\). The ideal condition is equivalent to \(A\wedge V_d\subseteq W\). Indeed the only potentially nonzero brackets with \(I\) are the wedges of vectors in \(A\) with vectors in \(V_d\). Conversely, every such pair of subspaces and every linear lift \(f:A\to(\bigwedge^2V_d)/W\) determine exactly one ideal, namely the full preimage in \(V_d\oplus\bigwedge^2V_d\) of the graph of \(f\) modulo \(W\).

If \(\dim A=a\), then \((\bigwedge^2V_d)/(A\wedge V_d)\simeq\bigwedge^2(V_d/A)\) has dimension \(m_a=\binom{d-a}{2}\). If \(\dim(W/(A\wedge V_d))=b\), then there are \({m_a\brack b}_q\) choices for \(W\), and the space of lifts has dimension \(a(m_a-b)\). With \(c=m_a-b\), this gives the stated exact identity. For \(a=0\), it yields
\[
C_d=\sum_{c=0}^{N_d}{N_d\brack c}_q
\]
central ideals. For \(a=1\), it yields
\[
T_{1,d}={d\brack1}_q\sum_{c=0}^{M_d}{M_d\brack c}_q q^c.
\]
Write \(T_{a,d}\) for the analogous count with projection rank \(a\).

**2. Theta asymptotics for Gaussian-binomial sums.** Put \(P_n(q)=\prod_{j=1}^n(1-q^{-j})\), with \(P_0=1\) and \(P_\infty(q)=\prod_{j\ge1}(1-q^{-j})>0\). The standard product formula gives
\[
{n\brack c}_q=q^{c(n-c)}\frac{P_n(q)}{P_c(q)P_{n-c}(q)}.
\]
The ratio lies between \(1\) and \(P_\infty(q)^{-1}\), and tends to \(P_\infty(q)^{-1}\) whenever \(c,n-c\to\infty\). Completing the square in \(c(n-c)+hc\) and invoking dominated convergence for the uniformly Gaussian-bounded centered summands yields, for each fixed \(h\in\{0,1\}\),
\[
\sum_{c=0}^n {n\brack c}_q q^{hc}
=\frac{q^{(n+h)^2/4}}{P_\infty(q)}\bigl(\Theta_{[n+h]}(q)+o(1)\bigr).
\]
The parity condition records whether the maximizing center is an integer or a half-integer. The error vanishes along both parities, so the displayed formula is valid over the full sequence. The two theta factors are strictly different: Poisson summation for the Gaussian gives
\[
\Theta_0(q)-\Theta_{1/2}(q)=4\sqrt{\frac{\pi}{\log q}}\sum_{j\ge0}\exp\left(-\frac{\pi^2(2j+1)^2}{\log q}\right)>0.
\]
In particular the four-periodic ratio is not constant.

Consequently,
\[
C_d=\frac{q^{N_d^2/4}}{P_\infty(q)}(\Theta_{[N_d]}(q)+o(1)),
\]
and, because \({d\brack1}_q=q^{d-1}(1-q^{-d})/(1-q^{-1})\),
\[
T_{1,d}=\frac{q^{d-1+(M_d+1)^2/4}}{(1-q^{-1})P_\infty(q)}(\Theta_{[M_d+1]}(q)+o(1)).
\]
The exponent difference simplifies exactly to
\[
d-1+\frac{(M_d+1)^2-N_d^2}{4}=-\frac{d^3}{4}+d^2-\frac d2.
\]
In particular, \(T_{1,d}/C_d\to0\).

**3. Higher projection ranks are negligible.** For \(d\ge5\) and \(2\le a\le d\), the convex function \(m_a+a=\binom{d-a}{2}+a\) is bounded above by its endpoint value \(N_d-2d+5\). By the Gaussian coefficient bound from Step 2, \(a(d-a)\le d^2/4\), and completion of the square,
\[
T_{a,d}\le P_\infty(q)^{-2}(N_d+1)
q^{d^2/4+(N_d-2d+5)^2/4}.
\]
On the other hand, taking the largest term in the \(a=1\) sum gives
\[
T_{1,d}\ge q^{d-1+\lfloor(M_d+1)^2/4\rfloor}.
\]
Thus
\[
\frac{\sum_{a=2}^dT_{a,d}}{T_{1,d}}
\le d(N_d+1)P_\infty(q)^{-2}
q^{-\Delta_d+1/4}\longrightarrow0,
\]
where \(\Delta_d=d^3/4-2d^2+23d/4-25/4\to\infty\). (This estimate is needed only for sufficiently large \(d\).)

**4. Passage to probabilities.** The total number of ideals is \(C_d+T_{1,d}+\sum_{a\ge2}T_{a,d}\). Step 3 makes the noncentral portion asymptotic to \(T_{1,d}\); Step 2 makes the denominator asymptotic to \(C_d\). Taking the ratio proves the stated theta-modulated cubic law. Step 3 also proves the conditional concentration on projection rank one.

## Verification
Run `python verify.py` from the directory containing this document and the script. The code independently enumerates row-reduced subspaces of \(L_d\) and tests ideal closure directly, without using the counting identity in the membership test. It exhaustively checks \((d,q)=(2,2),(2,3),(3,2),(3,3)\): respectively \(16,28,2825,56632\) subspaces. For example, \((d,q)=(3,2)\) yields \(45\) ideals and projection-rank counts \((16,21,7,1)\), while \((3,3)\) yields \(94\) ideals and \((28,52,13,1)\). The script also evaluates the finite exact formula and asymptotic estimates for multiple larger ranks at \(q=2,3\). These are checks of small instances and limiting diagnostics, **not** a substitute for the unrestricted proof.

## Relationship to prior work
Ideal and normal-subgroup zeta functions of free class-two nilpotent Lie rings and associated groups have long been studied. Voll (2004, 2005) treats the zeta functions and index-growth questions at fixed generator rank. Carnevale, Schein, and Voll (2019 preprint; revised 2023), especially Section 5.2, give strong exact ideal-zeta coverage for free class-two Lie rings; the elementary finite-field projection count above is *not* presented as new in isolation. Bauer and Schein (2022 preprint, 2023 journal) treat ideal growth of amalgamated class-two algebras. Siconolfi, Vantomme, and Voll (2023 preprint) treat subgroup and subalgebra zeta functions. These works provide foundational enumeration context, but the inspected results concern index growth or structural formulae, not the fixed-field \(d\to\infty\) probability of a noncentral ideal, its explicit cubic exponent, four-periodic theta constant, and conditional rank-one law. Searches found no matching statement; absence of matches is not proof of publication priority.

## Limitations
The result concerns uniformly sampled \(\mathbb F_q\)-linear Lie ideals of the finite-field Lie algebra, not ideals of the integral Lie ring or arbitrary subalgebras. The generator rank tends to infinity while \(q\) remains fixed; no uniformity in a simultaneously growing field size is claimed. The sharp asymptotic has an implicit \(o(1)\) depending on \(q\), not a stated effective rate. A substantially more general prior asymptotic enumeration theorem might imply this statement, and independent audit/publication-priority certification has not been performed.

## References
1. A. Carnevale, M. M. Schein, C. Voll, *Generalized Igusa functions and ideal growth in nilpotent Lie rings*, arXiv:1903.03090, initially public 2019-03-07, particularly Sections 1.1 and 5.2. https://arxiv.org/abs/1903.03090
2. T. Bauer, M. M. Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations*, arXiv:2202.10865, initially public 2022-02-22, particularly Theorem 1.1. https://arxiv.org/abs/2202.10865
3. C. Voll, *Normal subgroup growth in free class-2-nilpotent groups*, arXiv:math/0409383, initially public 2004-09-21, especially Theorems 2–4. https://arxiv.org/abs/math/0409383
4. V. Siconolfi, M. Vantomme, C. Voll, *Subgroup growth in free class-2-nilpotent groups*, arXiv:2305.19665, initially public 2023-05-31, especially Introduction and Sections 4–6. https://arxiv.org/abs/2305.19665
