# Sharp \(6N-3\) rotational degree for prescribed concentric Floquet data

## Finding
Fix an integer \(N\ge1\), radii \(0<r_1<\cdots<r_N\), physical periods \(T_i>0\), and transverse Floquet multipliers \(\mu_i>0\) with \(\mu_i\ne1\). Let \(s_i=r_i^2\) and \(A(s)=\prod_{j=1}^{N}(s-s_j)\). Among rotation-equivariant planar real polynomial vector fields
\[
\dot x=xQ(x^2+y^2)-y\Omega(x^2+y^2),\qquad
\dot y=yQ(x^2+y^2)+x\Omega(x^2+y^2),
\]
where \(\Omega(s)>0\) for every \(s\ge0\), exactly the prescribed circles are nonconstant periodic orbits, and all are hyperbolic, the data are realizable **if and only if** the signs of
\[
\frac{\log\mu_i}{A'(s_i)}
\]
are identical for all \(i\). (For \(N=1\) this condition is automatic.) Every compatible data set has a realization of total polynomial degree at most \(6N-3\). This is the **sharp worst-case degree** within the stated rotation-equivariant class: for every fixed collection of positive radii and periods, some compatible nonunit multipliers require degree at least \(6N-3\), while other multiplier choices may admit smaller degree.

## Assumptions and scope
A rotation-equivariant polynomial field has the displayed form with real univariate polynomials \(Q,\Omega\); its degree is the maximum total degree of its two Cartesian components. Positive angular speed rules out equilibrium circles and fixes counterclockwise physical time. The prescribed circles are required to be the **only nonconstant periodic trajectories** and the only positive-radius invariant circles. No global forward-completeness or boundedness is asserted. A Floquet multiplier is the nontrivial derivative of a transversal first-return map over **one physical period**. All input radii are pairwise distinct and strictly positive; multipliers equal to one are excluded.

## Proof
**1. Necessity.** Put \(s=x^2+y^2\) and \(\theta=\arg(x+iy)\). The polar equations are
\[
\dot s=2sQ(s),\qquad \dot\theta=\Omega(s).
\]
A nonconstant periodic trajectory can occur only at a positive zero of \(Q\); with positive angular speed every such zero is a periodic invariant circle. The hypothesis therefore makes the \(s_i\) all the positive roots of \(Q\). Hyperbolicity makes each root simple. Factor \(Q(s)=A(s)P(s)\). Since \(P\) has no zeros on \((0,\infty)\), it has a constant nonzero sign there. The physical-time period of the \(i\)-th circle is \(2\pi/\Omega(s_i)\) and its nontrivial Floquet multiplier is exactly
\[
\exp\bigl(2s_iQ'(s_i)T_i\bigr)
=\exp\bigl(2s_iA'(s_i)P(s_i)T_i\bigr).
\]
Hence \(P(s_i)=\log\mu_i/(2s_iT_iA'(s_i))\). The common sign of \(P\) proves necessity, including alternating attracting and repelling circles.

**2. Construction.** Let \(\sigma\in\{-1,1\}\) be that common sign, and set
\[
h_i=\frac{\log\mu_i}{2\sigma s_iT_iA'(s_i)}>0,\qquad
\omega_i=\frac{2\pi}{T_i}>0.
\]
Define Lagrange basis polynomials
\[
\ell_i(s)=\prod_{j\ne i}\frac{s-s_j}{s_i-s_j},\qquad \sum_i\ell_i(s)=1,
\]
and set
\[
H(s)=\sum_{i=1}^{N}h_i\ell_i(s)^2,\qquad
\Omega(s)=\sum_{i=1}^{N}\omega_i\ell_i(s)^2,\qquad
Q(s)=\sigma A(s)H(s).
\]
Because the \(\ell_i\) sum to one, they never vanish simultaneously. Thus \(H\) and \(\Omega\) are strictly positive for **all real** \(s\), and \(H(s_i)=h_i\), \(\Omega(s_i)=\omega_i\). The roots of \(Q\) in \((0,\infty)\) are exactly the simple \(s_i\). The equations from step 1 yield the required period and multiplier on every circle, proving sufficiency and ruling out additional periodic orbits. Since \(\deg H,\deg\Omega\le2N-2\) and \(\deg Q\le3N-2\), the Cartesian polynomial degree is at most \(2(3N-2)+1=6N-3\).

**3. Sharp positive interpolation lemma.** For fixed \(0<s_1<\cdots<s_N\), \(N\ge2\), there is a positive \(\varepsilon_0\) such that, whenever \(0<\varepsilon<\varepsilon_0\), no polynomial \(P\) of degree at most \(2N-3\), strictly positive on \((0,\infty)\), can satisfy \(P(s_1)=1\) and \(P(s_i)=\varepsilon\) for all \(2\le i\le N\).

Indeed, if not, choose \(\varepsilon_m\downarrow0\) and corresponding positive polynomials \(P_m\) of degree at most \(2N-3\). Regard their coefficient vectors in the fixed finite-dimensional polynomial space. If bounded, a subsequence converges to a nonnegative polynomial \(P\) with \(P(s_1)=1\), \(P(s_i)=0\) for \(i\ge2\). Every zero at an interior point of a nonnegative nonzero real polynomial has even multiplicity; thus \(\deg P\ge2(N-1)>2N-3\), a contradiction. If unbounded, divide coefficients by their norm and take a subsequence. The normalized limit is a nonzero polynomial \(R\ge0\), of degree at most \(2N-3\), with \(R(s_i)=0\) for **all** \(i\), since the unnormalized nodal values are bounded. Even multiplicity now gives \(\deg R\ge2N>2N-3\), again a contradiction. This proves the lemma without numerical extrapolation.

**4. Sharpness for polynomial flows.** Fix the radii and periods. For \(N\ge2\), choose \(0<\varepsilon<\varepsilon_0\) and positive nodal data \(h_1=1\), \(h_2=\cdots=h_N=\varepsilon\). Prescribe multipliers
\[
\mu_i=\exp\bigl(2s_iT_iA'(s_i)h_i\bigr).
\]
These are positive, nonunit, and satisfy the compatibility condition with \(\sigma=1\). In **any** admissible realization \(Q=A P\), the absence of any other positive-radius invariant circle implies \(P\) has no positive root, and the specified multipliers force \(P(s_i)=h_i>0\). Thus \(P>0\) on \((0,\infty)\), and the lemma forces \(\deg P\ge2N-2\); consequently \(\deg Q\ge3N-2\). The degree of the vector field is at least \(2\deg Q+1\), because the radial and angular homogeneous polynomial components cannot cancel: their dot product with the radial and tangential unit vectors separates them. The lower bound is \(6N-3\). For \(N=1\), any hyperbolic circle requires a nonconstant \(Q\), so the minimal degree is at least three, attained by the construction.

For a concrete two-circle lower-bound witness, take \(s_1=1\), \(s_2=4\), \(T_1=T_2=2\pi\) and \(h_1=1\), \(h_2=1/10\). The corresponding multipliers are \(\mu_1=e^{-12\pi}\) and \(\mu_2=e^{24\pi/5}\). Any affine interpolant through these positive \(h\)-values is \(P(s)=1-3(s-1)/10\), which vanishes at \(s=13/3>4\), so no admissible degree-seven rotational field exists; degree nine is attained.

## Verification
The standalone `verify.py` uses Python standard-library exact rational polynomial arithmetic. It constructs Lagrange-square polynomials for \(1\le N\le6\), checks all node values, the factorization, radial derivatives and required Floquet exponents, and verifies the degree bounds. It also gives an exact two-circle witness against affine positive interpolation. Run `python3 verify.py` from this package; the expected output is `VERIFY_OK`. The finite tests do not establish the infinite theorem: the all-\(N\) proof is the four-step argument above.

## Relationship to prior work
Margalef-Bentabol and Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields* (first public preprint 2015-07-02, arXiv:1507.00698v1), prove realization of prescribed limit-cycle configurations with periods, multiplicities and stability **signs**, including explicit degree upper bounds (Theorems 1.2, 4.2 and 5.2). This finding does not claim that general qualitative realization theorem as new. The specific contribution is exact independent quantitative transverse Floquet multipliers at fixed concentric circles together with a sharp **minimax degree in the restricted rotation-equivariant class**, which is not stated by those theorems. Positive polynomial interpolation itself is standard; its obstruction is applied here to the inverse Floquet problem. A general method elsewhere might imply part of the construction; no global novelty certification is claimed.

## Limitations
The sharp bound is not asserted among **all** planar polynomial vector fields. The compatibility condition depends on requiring exactly the specified positive-radius invariant circles and hyperbolicity; inserting extra invariant circles changes the condition. The result is not about nonlinear or noncircular cycles, does not classify other dynamics of the vector field, and does not require the polynomial flow to be forward complete at infinity. The exponent \(6N-3\) is a **worst-case** upper and lower bound, not the exact minimum for every admissible target list. No external independent verification has been performed.

## References
1. J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698v1, publicly submitted 2015-07-02; see Theorems 1.2, 2.1, 4.2 and 5.2. https://arxiv.org/abs/1507.00698; full text https://arxiv.org/html/1507.00698v2.
2. J. Llibre and G. Rodríguez, *Configurations of limit cycles and planar polynomial vector fields*, J. Differential Equations (2004), identified and discussed as predecessor in reference 1. No full-text comparison of this predecessor is claimed.
