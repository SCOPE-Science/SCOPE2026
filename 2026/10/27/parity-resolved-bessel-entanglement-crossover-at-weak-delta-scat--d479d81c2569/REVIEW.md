# Independent mathematical audit

## correctness

PASS

The delta amplitudes have t/r=i k/gamma and |r|=cos(theta), giving the stated coin after removing a common phase. With D(q)=diag(e^(iq),e^(-iq)) and A=D(q)sigma_x, A is Hermitian with A^2=I. The two-step multiplier differs uniformly from exp(2i theta cos(q) A) by O(theta^2): the cross term is 2i sin(theta)cos(theta)cos(q) A. Telescoping the unitary products controls the even factor by O(n theta_n^2), and on odd lengths the leftover multiplier differs from A by O(theta_n). The final scaled-phase difference is at most |n theta_n-tau|. This tends to zero for every allowed sequence, implies norm convergence in the phase convention used, then trace-norm convergence of the reduced coin by contractivity. For the initial x-directed Bloch vector the limit uses an axis a=(cos q,-sin q,0); the pointwise x-component is cos^2(q)+(-1)^n sin^2(q)cos(2 tau cos q). Reflection q -> -q reverses the other two components. The weighted cosine average equals [J_0(2 tau)+J_2(2 tau)]/2=J_1(2 tau)/(2 tau), with value 1/2 at zero. Thus the normalized Bloch radii and the larger eigenvalues (3 +/- B)/4 have the claimed signs and factors. The bound |B|<=1 follows from the same integral, so strict monotonicity of h_2 on [1/2,1] gives equality exactly at B=0, with sign changes at the simple positive zeros. h_2'(3/4)=-log_2(3), and J_1(2 tau)/tau has leading cos(2 tau-3 pi/4)/(sqrt(pi) tau^(3/2)), yielding the claimed signed envelope and remainder. The endpoints are pure versus maximally mixed at tau=0, and the common entropy tends to h_2(3/4) for diverging tau on the limiting curves only.

## originality

PASS

Credit the explicit parity-resolved reduced-state and entropy scaling functions, not the energy-dependent coin, the swap endpoint, or the stroboscopic continuous-time dynamics or their global Bessel propagators. The source scattering paper gives an exact finite-step spectral integral for the same setup and recognizes weak-transmission nonuniformity; it takes a fixed-wavenumber long-time limit, not the joint observable crossover. General continuum theory is strong enough to recover the even limiting evolution and, with a remaining swap-and-shift, the odd one. Extracting the two reduced-state functions requires the momentum-dependent overlaps with the initial coin, retaining the oscillating term instead of averaging it out, and evaluating its weighted Bessel integral. The inspected statements do not give this reduced observable or an equivalent already evaluated contrast. The crossings and envelope are consequences of the explicit new contrast, not separate priority claims.

## value

PASS

The loss of uniform entanglement decay at vanishing transmission is posed by the same physical model in prior work, independently of any Bessel calculation. The two explicit state functions quantify what fixed-k equilibration and the swap endpoint cannot tell an observer working at n k/gamma of order one: how much coin coherence survives, when the parities first and repeatedly coincide, and how their contrast decays. The weighted Bessel reduction is the useful analytic output, rather than a new continuum walk or a routine check at zero transmission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
