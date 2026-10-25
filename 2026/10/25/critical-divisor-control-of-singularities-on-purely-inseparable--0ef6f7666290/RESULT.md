# Critical-divisor control of singularities on purely inseparable plane curves

## Finding

Let \(k\) be an algebraically closed field of prime characteristic \(p>0\), and let \(f(x,y)\) be a squarefree homogeneous binary form of degree \(p\). Consider the integral plane curve

\[
X_f=V(z^p-f(x,y))\subset\mathbb P^2_k.
\]

The singular points of \(X_f\) correspond exactly to the zeros of the differential of the local coefficients of \(f\) on \(\mathbb P^1\). If the first nonconstant term at such a point has order \(m\), then \(2\le m\le p-1\) and the completed local ring is

\[
\widehat{\mathcal O}_{X_f,P}\cong k[[u,v]]/(v^p-u^m).
\]

Thus the value semigroup is \(\langle m,p\rangle\) and the delta invariant is \(\delta_P=(p-1)(m-1)/2\). The critical orders satisfy \(\sum_P(m_P-1)=p-2\); consequently the sum of all delta invariants is \((p-1)(p-2)/2\), the arithmetic genus of a plane curve of degree \(p\). The normalization of \(X_f\) is therefore \(\mathbb P^1_k\).

For \(p=5\), the squarefree form \(f=x^5+x^2y^3+xy^4\) gives exactly two singularities, with value semigroups \(\langle2,5\rangle\) and \(\langle3,5\rangle\), and delta invariants \(2\) and \(4\), respectively.

## Assumptions and scope

The field is algebraically closed of prime characteristic \(p\). The form \(f\) is homogeneous of degree \(p\) and has \(p\) distinct geometric roots on \(\mathbb P^1\). The result does not assert the same local normal forms for degree \(p^r\) with \(r>1\), for non-squarefree forms, or over a nonperfect ground field without geometric base change. The characteristic-five example is a concrete member of the \(\mu_p\)-normal curve family used in constructions of strongly isotrivial elliptic surfaces.

## Proof

Write \(h(t)=f(t,1)\) on the chart \(y\ne0\), and \(g(s)=f(1,s)\) on the chart \(x\ne0\). Since \(f\) has a simple root, it is not a \(p\)-th power in \(k(t)\). Hence \(Z^p-h(t)\) is irreducible over \(k(t)\), so \(X_f\) is integral. The projection \([x:y:z]\mapsto[x:y]\) is a finite purely inseparable map of degree \(p\).

For \(F=z^p-f(x,y)\), the derivative \(F_z\) vanishes identically in characteristic \(p\). Euler's identity gives \(xf_x+yf_y=pf=0\). On the chart \(y=1\), the singularity condition is therefore \(h'(t)=0\); the chart at infinity gives the corresponding condition \(g'(s)=0\). A root of \(f\) is simple, so it is not a zero of this differential. Thus every singular point lies over a critical point where the local coefficient is nonzero, and there are no other singularities.

At a critical point, choose a local parameter \(u\) and write

\[
f=f_0+a_m u^m+a_{m+1}u^{m+1}+\cdots,
\qquad a_m\ne0,
\]

where \(m\ge2\) is minimal. Squarefreeness rules out \(m=p\): otherwise the local coefficient would be \(f_0+a_pu^p\), a \(p\)-th power over \(k\), forcing the binary form to have a repeated root. Hence \(2\le m\le p-1\), and \(m\) is invertible in \(k\). After extracting an \(m\)-th root of the unit multiplying \(u^m\), a formal change of parameter puts the local equation into the form \(v^p=u^m\).

Because \(\gcd(m,p)=1\), the normalization of \(k[[u,v]]/(v^p-u^m)\) is \(k[[s]]\), with \(u=s^p\) and \(v=s^m\). Its value semigroup is \(\langle p,m\rangle\), whose number of gaps is \((p-1)(m-1)/2\); this is \(\delta_P\).

The differential of the local coefficient is a global section of \(\mathcal O_{\mathbb P^1}(p-2)\): on overlaps, differentiating the transition factor of degree \(p\) produces no extra term because the characteristic is \(p\). It is nonzero, since otherwise \(f\) would be a \(p\)-th power. Its zero divisor therefore has degree \(p-2\), and at a critical point with local exponent \(m_P\) its multiplicity is \(m_P-1\). Thus

\[
\sum_P\delta_P=\frac{p-1}{2}\sum_P(m_P-1)
=\frac{(p-1)(p-2)}2.
\]

The right side is the arithmetic genus of a plane curve of degree \(p\). The normalization genus is the arithmetic genus minus the sum of the delta invariants, hence zero; over an algebraically closed field the normalization is \(\mathbb P^1_k\).

For the characteristic-five example, \(h(t)=t^5+t^2+t\) has derivative \(2t+1\), whose only root is \(t=2\), and \(h(2)=3\ne0\). Also \(f(1,0)=1\), so \(f\) has five distinct roots. Near \(t=2\), writing \(t=2+u\) and \(z=z_0+v\), with \(z_0^5=3\), gives \(v^5=u^2(1+u^3)\); the unit can be absorbed into \(u\), yielding \(v^5=U^2\). At infinity, put \(s=y/x\) and \(z/x=1+v\); then \(v^5=s^3(1+s)\), which becomes \(v^5=U^3\). The corresponding delta invariants are \(2\) and \(4\), and their sum \(6\) equals the arithmetic genus of a plane quintic. The included script checks the finite-field arithmetic and semigroup gap counts for this example; the general theorem is proved above, not inferred from computation.

## Verification

The proof uses the Jacobian criterion, Euler's identity in characteristic \(p\), the formal coordinate change absorbing a unit, the numerical-semigroup gap formula for coprime generators, and the plane-curve genus formula. The reproducibility artifact `verify_curve.py` uses only the Python standard library. It checks that the characteristic-five polynomial is squarefree, verifies the two critical orders and local expansions, counts the gaps in \(\langle2,5\rangle\) and \(\langle3,5\rangle\), and confirms that the delta sum equals \(6\). These finite checks verify the displayed example only; they are not used as a substitute for the general proof.

## Relationship to prior work

Fong and Maccan study the family \(z^{p^r}=f(x,y)\) with squarefree \(f\), its \(\mu_{p^r}\)-normality, fixed points, and the associated strongly isotrivial elliptic surfaces. Brion gives the local structure and a Hurwitz-type arithmetic-genus formula for equivariantly normal curves. Those results explain the family and its total genus defect, but the inspected statements do not identify the individual free-point singularity semigroups from the critical divisor of \(f\). The local semigroups \(\langle m,p\rangle\) themselves are standard plane-branch invariants; the contribution here is the global correspondence between the critical divisor of a squarefree degree-\(p\) binary form and the complete singularity profile of this specific inseparable plane-curve family.

For the characteristic-five example, the five simple roots of \(f\) are the five fixed points of the \(\mu_5\)-action scaling \(z\); the two singularities found above lie at free points. When \(E\) is an ordinary elliptic curve containing \(\mu_5\), the established contracted-product construction gives the corresponding elliptic surface with five multiple fibers and Kodaira dimension one. This is contextual motivation, not a new claim about the surface classification.

## Limitations

The statement concerns local analytic types and delta invariants, not modality, deformation classes, or automorphism groups of the branches. It does not extend as stated to exponent \(p^r\) for \(r>1\), where critical orders can interact with the characteristic in additional ways. The standard local classification literature may contain overlapping descriptions of individual monomial branches; no novelty is claimed for those local models in isolation. Independent mathematical audit has not been performed.

## References

1. Pascal Fong and Matilde Maccan, *Isotrivial elliptic surfaces in positive characteristic*, arXiv:2405.11602, first posted 2024-05-19; see Theorem A, Lemma 3.11, and Example 3.13.
2. Michel Brion, *Equivariantly normal varieties for diagonalizable group actions*, arXiv:2405.12020, first posted 2024-05-20; see Theorem 1 and the arithmetic-genus formula (1.1).
3. Muhammad Ahsan Binyamin, Gert-Martin Greuel, Khawar Mehmood, and Gerhard Pfister, *Classification of Unimodal Parametric Plane Curve Singularities in Positive Characteristic*, arXiv:2301.09409, first posted 2023-01-23; local plane-branch and value-semigroup context.
4. Hong-Duc Nguyen, *Parametrization simple irreducible plane curve singularities in arbitrary characteristic*, arXiv:1901.02758, first posted 2019-01-09; local parametrization and singularity-invariant context.
