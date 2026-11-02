# Independent mathematical audit

## correctness

PASS

For xdot=-x+u, ydot=u-xy with u≥0, x0,y0≥0 fixed and finite T, variation-of-constants gives x(t)=x0e^-t+u(1-e^-t) and exact y integral. Differentiate at u=0 to obtain C_u(0+,T)=P(T,x0)-y0Q(T,x0), with P,Q strictly positive, and verify x0=0,T=3,y0=2 gives -1/2+2e^-3<0. Near t=0, 1-e^-t is squeezed between c_delta t and t; Gaussian model u∫0^t exp[-a u(t²-s²)/2]ds has integrated asymptotic (log u)/(2a) from zH(z)→1. Bounds and O(1) contribution away from zero imply C(u,T)/log u→1/2, independently of initial loads. Negative onset and divergence imply at least one interior positive-input global minimum. Claims neither uniqueness nor a finite-dose expansion.

## originality

PASS

Same scalar IFFM1/IFFL1 ODE is studied by Wafi–de Oliveira–Sontag 2026 and Gupta–Sontag 2025, but their monotone cumulative-dose results impose an adapted initial output y0=1. Candidate allows arbitrary independent output preload; large preloads violate onset monotonicity, and boundary-layer coefficient 1/2 is not stated by inspected antecedents. No exact equivalent indexed Resultary claim, though singular perturbation folklore is an explicit risk.

## value

PASS

Identifies mathematically sharp initial-slope threshold for the same experimentally motivated adaptation motif and proves a robust open family of nonmonotone dose responses without contradicting the original preadapted monotonicity theorem; high-dose 1/2 log law supplies rebound mechanism. A meaningful boundary of a published qualitative guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
