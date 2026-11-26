# Independent mathematical audit

## correctness

PASS

For 0<T<1 the even overlap is L²−t² on |t|≤h and (1−|t|)²−h² on h≤|t|≤L, with h=T/2, L=1−T/2. Its second derivative has densities −2 and +2 and jumps −2(1−T) at ±h and T at ±L. Fourier transforming gives the stated general formula for F=(2πν)²A. At T=2/3 the two cosine coefficients balance and L=2h; the trig factorization gives the stated sin² factor and Q and the limit 10/27 at zero. The endpoint signs of Q alternate. On a positive-sine half-period, a root has cos x<−1/2, hence Q'<0. On a negative-sine half-period Q'>0 at every root: this is immediate for cos x≥0; otherwise cos x>−1/2 and −sin x>sqrt(3)/2 dominate the possible negative contribution, using x>π. Nonzero derivatives give isolated strict crossings, so there cannot be two roots of the same crossing orientation in one interval. Q=3 at positive sine-square lattice roots, giving exact double zeros there; zero frequency is not a root. The two simple plus one double zero per Doppler period 3 give the two counts. For c=2π/3 or 4π/3 let x_0=2πk+c and ε=1/x_0. The root equation in δ=x−x_0 is 1+2cos(c+δ)+2ε sin(c+δ)/(1+εδ)=0; implicit differentiation at ε=0 gives δ'(0)=1, hence the quoted positive shift after rescaling. For the Hessian, differentiate F in (T,ω) with ω=2πν. At ω=6πn and T=2/3, F and its first derivatives vanish, and (F_TT,F_Tω,F_ωω)=(0,−2ω/3,4/9). Dividing by ω² and applying ∂_ν=2π∂_ω gives the displayed Hessian. Its indefinite nondegenerate quadratic form gives two transverse analytic zero branches by the analytic Morse lemma, with slopes 0 and 9n.

## originality

PASS

Credit the standard piecewise-polynomial Fourier and analytic nodal-set methods. The supported distinction is the complete real-Doppler classification at the geometrically balanced lag together with the nondegenerate two-variable crossings and explicit tangent slopes. The strongest same-window comparisons concern the Zak transform or Gabor frame operator, not this self-ambiguity slice. General local exclusion theorems do not yield remote root counts or Hessians, and the standard Haar step at the same lag has simple zeros on a single regular branch, not these double zeros and crossings. This bounded comparison does not certify first publication.

## value

PASS

The standard hat spline and its self-ambiguity are natural, and the slice is dictated by the overlap geometry: the interior knots lie halfway to the support endpoints precisely where the two boundary-jump weights balance. The consequence is more informative than a transform evaluation: it gives two interlaced simple-root sequences, exact double multiplicity on the lattice, and resolves whether each double trace zero is an isolated degeneracy or a transverse crossing under a delay perturbation. The explicit local geometry is useful even without a nearby-lag global census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
