# Six Milnor-27 points and an Euler-minus-168 smoothing of the rank-twelve quartic model

## Finding

Let \(M=\mathbb P_{\mathbb P^1}(\mathcal O(3)^{\oplus2}\oplus\mathcal O(4)\oplus\mathcal O)\), using the convention that its fiber coordinates \([X:Y:Z:W]\) have coordinate-divisor classes \(H+3F,H+3F,H+4F,H\), where \(H\) is the relative hyperplane class and \(F\) is the pullback of a base point. Set \(D=-K_M=4H+12F\). Inside \(|D|\) consider the special quartic \(Q\) of [1], which on one base chart is

\[
ZW\bigl(Z+(v^2+1)^2W\bigr)\bigl(Z+(v^2-1)^2W\bigr)=XY(X+25Y)(X+9Y).
\]

**Theorem.** The six isolated singularities of \(Q\) have **threefold** Milnor number \(27\) each. The complete anticanonical linear system has smooth members, so \(Q\) admits a projective one-parameter smoothing \(Q\leadsto T\) to a smooth Calabi–Yau threefold. Every smooth member of \(|D|\) has

\[
e(T)=-168.
\]

For the six-divisor projective crepant resolution \(Y\to Q\) of [1], \(e(Y)=48\). Thus the transition changes Euler characteristic by \(216\), consisting of six equal local contributions \(36\). A general smooth \(T\) additionally satisfies \(h^{1,1}(T)\ge5\), hence \(h^{2,1}(T)\ge89\); **no exact Hodge pair is asserted**.

## Assumptions and scope

All varieties and singularities are over \(\mathbb C\). A smooth member means any smooth divisor of the indicated complete anticanonical linear system; the Picard lower bound refers to a general member with a squarefree forced binary quartic. The Burek quartic and its isolated singularities, local weighted initial forms, projective crepant resolution, degree-two del Pezzo exceptional divisors, and \(e(Y)=48\) are established in [1, §§3–4 and Remark 8.4]. The statements below about global smoothing, **threefold** Milnor number, and Euler characteristic of smooth members are the new calculations.

## Proof

**1. Existence of a smooth global anticanonical member and smoothing.** A monomial \(X^aY^bZ^cW^d\), with \(a+b+c+d=4\), is permitted in a section of \(D\) precisely when its base coefficient has degree \(12-3a-3b-4c\ge0\). The sections \(W^4\), \(X^4\), and \(Y^4\), multiplied where necessary by base forms of the required nonnegative degree, show that the common base locus of \(|D|\) is exactly the section \(B=\{X=Y=W=0\}\simeq\mathbb P^1\). The monomial \(Z^3W\) has base degree zero and occurs with an unrestricted **constant** coefficient. On the local chart \(Z\ne0\), its derivative in the \(W\) direction is nonzero along \(B\) whenever this coefficient is nonzero. Every such anticanonical hypersurface is therefore smooth along \(B\). Bertini's theorem applied off the base locus implies that a general anticanonical hypersurface is smooth everywhere. Since smooth divisors form a nonempty Zariski-open locus and \(Q\) belongs to the same projective linear system, choose a smooth section \(s_1\) generically so that the pencil of sections \(s_0+t s_1\), with \(s_0\) defining \(Q\), gives a flat projective one-parameter smoothing, smooth for generic nonzero \(t\). Flatness follows because this pencil is a relative effective Cartier divisor on the smooth ambient product over the parameter away from the identically-zero member. Adjunction yields \(\omega_T\simeq\mathcal O_T\). Since \(H^j(M,\mathcal O_M)=0\) for \(j>0\), Serre duality and \(0\to K_M\to\mathcal O_M\to\mathcal O_T\to0\) give \(H^1(T,\mathcal O_T)=H^2(T,\mathcal O_T)=0\). Thus \(T\) is Calabi–Yau in the conventional projective sense.

**2. Threefold Milnor numbers (not Milnor numbers of K3 fibers).** By [1, Lemma 4.1 and Proposition 4.2], in four analytic ambient variables \((x,y,s,z)\) each singularity has weighted initial equation

\[
f_4=\lambda z^2+\mu s^4-q(x,y),\qquad q(x,y)=xy(x+25y)(x+9y),\qquad \lambda\mu\ne0,
\]

for weights \((1,1,1,2)\) and weighted degree \(4\). The four factors of the binary quartic \(q\) have distinct projective roots; the partials \(q_x,q_y\) therefore have no common projective zero and form a homogeneous cubic complete intersection of colength \(3\cdot3=9\). The Jacobian ideal of \(f_4\) is \((q_x,q_y,s^3,z)\), whose local quotient has dimension \(9\cdot3=27\). The standard semiquasihomogeneous Milnor-number theorem applies to the higher-weight terms of the actual germs, so \(\mu(Q,p)=27\) at **each of all six singularities**. The \(9\) appearing in [1, Remark 8.4] is instead the Milnor number of a singular **two-dimensional quartic K3 fiber** \(\{z^2-q(x,y)=0\}\) and does not determine the threefold Milnor number.

**3. Euler characteristic of the smooth anticanonical hypersurface.** In the integral Chow ring of \(M\),

\[
F^2=0,\quad H(H+3F)^2(H+4F)=0,\quad \int_M FH^3=1,\quad \int_M H^4=-10.
\]

The relative Euler sequence and the tangent sequence of the base give

\[
c(T_M)=(1+2F)(1+H+3F)^2(1+H+4F)(1+H).
\]

Thus \(c_1(T_M)=D\), \(c_2(T_M)=6H^2+38FH\), and \(c_3(T_M)=4H^3+42FH^2\). Adjunction gives \(c_3(T_T)=\bigl(c_3(T_M)-c_2(T_M)D+c_1(T_M)D^2-D^3\bigr)|_T\). Multiplying by \([T]=D\) and setting \(F^2=0\), the top-degree term is

\[
D\bigl(c_3-c_2D+c_1D^2-D^3\bigr)=-80H^4-968FH^3.
\]

Gauss–Bonnet therefore gives \(e(T)=-80(-10)-968=-168\). This integral is independent of which smooth member \(T\) is chosen.

**4. Independent local Euler calculation and transition.** Burek's resolution \(Y\to Q\) has six exceptional surfaces \(E_i\), each a degree-two del Pezzo double plane branched over a smooth genus-three quartic, so \(e(E_i)=10\); [1, Remark 8.4] computes \(e(Y)=48\). Replacing each exceptional surface by its singular point gives \(e(Q)=48-6(10-1)=-6\). A smoothing Milnor fiber of an isolated complex threefold hypersurface singularity of Milnor number \(27\) has Euler characteristic \(1-27=-26\). Thus \(e(T)=e(Q)+6(-26-1)=-168\), independently matching the Chern computation, and \(e(Y)-e(T)=216=6(9+27)\).

**5. A rigorous Hodge lower bound, not an exact Hodge classification.** Restrict an arbitrary global section in \(|D|\) to the relative hyperplane \(W=0\). Only the five monomials in \(X,Y\) of total degree four survive, each with constant base coefficient. For general \(T\), their binary quartic \(q_4(X,Y)\) is squarefree. On a smooth quartic K3 fiber, its four projective roots give four distinct coplanar lines \(L_1,\ldots,L_4\) through the point \([0:0:1:0]\). Their intersection matrix has diagonal \(-2\) by adjunction and off-diagonal \(1\) because each pair meets transversely at that point (the tangent plane of the smooth K3 fiber is \(W=0\); distinct planar line directions give transverse intersection on the surface). This \(4\times4\) matrix has eigenvalues \(1,-3,-3,-3\) and is nonsingular. The four divisors in \(T\) swept out by these lines therefore have independent restrictions to a general K3 fiber. The pullback of a base point has zero restriction but is nontrivial (it intersects a horizontal curve), hence \(\rho(T)\ge5\). Since a Calabi–Yau threefold has \(h^{2,0}=0\), \(h^{1,1}=\rho\); from \(-168=2(h^{1,1}-h^{2,1})\) follows \(h^{2,1}=h^{1,1}+84\ge89\). Determining the exact Picard rank is outside the theorem.

## Verification

The standalone Python 3 checker `verify.py` uses only the standard library. It checks the bundle relation, Chern-class expansions and integrated Euler number, the two independent Euler computations, allowed monomials on \(W=0\), nonzero resultant of the binary-quartic derivatives, the \(27\) local Jacobian colength, and the intersection-matrix rank. Run `python3 verify.py` after extracting the embedded file. These symbolic finite calculations check algebraic identities; smoothability and preservation of Milnor number are justified by the geometrical arguments and standard theorems above, not inferred from finite sampling.

## Relationship to prior work

Burek [1, Proposition 3.1, Lemmas 3.2/4.1, Proposition 4.2] supplies the ambient quartic, six singular points and crepant resolution. Remark 8.4 calculates the **fiber surface** Milnor number \(9\) and the resolved Euler characteristic \(48\), not the **threefold** Milnor number \(27\), existence of a global smoothing, or its \(-168\) Euler characteristic. The general frameworks of Milnor [2] and projective smoothing/K3 transitions [3] supply standard tools but not this numerical transition on Burek's specific threefold. The exact parameterized family, six total-space germs and numerical Euler jump were compared against accessible published mathematical-record entries and targeted primary-literature searches; no stronger covering statement was identified. This is not proof of historical uniqueness.

## Limitations

The result concerns the particular 2026 quartic and its full anticanonical smoothing system over \(\mathbb C\); the smoothing is **not claimed to preserve Mordell–Weil rank twelve** or the special elliptic fibration. The exact Hodge pair of the general smoothing is **not determined**. The former Hodge pair \((25,1)\) belongs to the crepant resolution, not to the smooth anticanonical fiber. The four-line argument only proves a lower bound for the latter's Picard number. The semiquasihomogeneous Milnor-number theorem and Milnor-fiber Euler formula are standard external inputs; their hypotheses are established explicitly above. The overlap assessment may not capture unpublished or obscure implicit computations.

## References

[1] Dominik Burek, *An elliptic Calabi–Yau threefold of Mordell–Weil rank twelve*, arXiv:2610.01276v1 (first public version 2026-10-01), §§3–4 and Remark 8.4, https://arxiv.org/html/2610.01276v1.

[2] John Milnor, *Singular Points of Complex Hypersurfaces*, Annals of Mathematics Studies 61 (1968), Milnor-fiber theorem and Euler characteristic.

[3] Stephen Coughlan, *K3 transitions and canonical 3-folds*, Bulletin of the London Mathematical Society 50 (2018), doi:10.1112/blms.12157, general transition context only.
