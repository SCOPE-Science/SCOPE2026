# Independent mathematical audit

## correctness

PASS

Independently reconstructed the unique periodic energy ovals via p(x)=exp(alpha x^4/4), V(x)=int_0^x p(s)^2(s+beta s^5)ds, and H=1/2 p² y²+V. Differentiating H cancels x³y² exactly. Positive V prime and even V imply one smooth closed orbit at each A and minimal original-time quarter-cycle integral 4int_0^A p/sqrt(2(V(A)-V(x)))dx. Substituting x=At yields exact J_{q,delta}, delta=(beta A^4)^-1. For 0<=q<=Q, 0<=R_q(t)<=3exp(Q/2) and -1/4<=d_q log w_q<=0 bound the relative errors uniformly even at the turning singularity, giving period convergence and TV density convergence. Set z=t^4 and g_q(v)=sqrt(v)e^{qv/2}; d_q(z)=E_q[v-z|v>=z] strictly decreases in z because the upper-truncated density has increasing hazard g/G, so d_q log w is strictly increasing in t. This proves strict MLR for q2>q1 and C decreases. At q=0, J_0=(1-t^6)/3 yields C0=2sqrt3/3 B(1/6,1/2) and rho0=6/(B sqrt(1-t^6)). For u=q(1-t), the exact boundary-layer F_q tends to 1-e^-2u; q>=2 yields an L1 majorant 4e e^-u/4 /sqrt(min(u,1)), hence sqrt(q)C(q)->2pi and the normalized law f(u)=(2/pi)e^-u/sqrt(1-e^-2u). The CDF and median follow by substitution. The inequality J_2<=e J_0, positive binomial expansion, sqrt2>7/5, sqrt3>17/10, sqrt(e)<5/3 produce exact S(2)>1575543/247000>44/7>2pi; continuity plus both endpoint limits forces an interior global maximum. Independent scipy desingularized nested quadrature gives C0=8.413092631952725 and C2=6.859953904491864, sqrt(2)C2=9.701439848986661; checked C monotonic at q in {0,.5,1,2,3,4,6,10}, strict unnormalized density-ratio ordering on seven t samples for q-pairs (0,1),(0,2),(1,4), and the rational inequality with Python Fraction. These bounded samples support, not replace, the all-q analytic argument. No uniqueness of maximum and no simultaneous arbitrary q->infinity/A->infinity limit are claimed.

## originality

PASS

Best-of-knowledge PASS for the full finite-q matched original-time position density, strict monotone likelihood ratio for all 0<=q1<q2<infinity, and rigorously strict overshoot of sqrt(q)C(q). The original global-center classification (2023), general position-dependent-mass Hamiltonian (2018), and October 11 exact fixed-parameter period theorem are already known and credited. The published closest same-flow theorem proves only separate alpha=0 and fixed alpha>0 amplitude limits and no finite-q occupation family. Its q->infinity boundary-layer kernel is explicitly antecedent, not claimed new. Current searches and genuine full prior-result reading found no dominating result for the three remaining mathematical claims; unsuccessful searches are not proof of uniqueness or priority. An inaccessible 2013 Lienard period-function article remains a named limited-access risk.

## value

PASS

This is a naturally motivated singular transition between the pure-quintic high-amplitude regime and the fixed-positive-velocity-square-coefficient regime of the same global-center family. The exact original-physical-time location law is an independent orbit-statistical invariant, not a time-rescaled trajectory artifact. Strict monotone likelihood ratios compare every upper-tail occupation event across all finite q, a structural fact beyond one moment or an endpoint constant. The rigorously certified overshoot of sqrt(q)C(q) falsifies a tempting monotone interpolation despite C itself decreasing; its eventual 2pi endpoint makes the global-max phenomenon nontrivial. A researcher studying parameter-dependent period laws or concentration near turning points could use the precise C(q), rho_q, and MLR result. The energy invariant and fixed-alpha endpoints are not themselves counted as new value, nor is an unproved uniqueness or a paper-sized downstream consequence required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
