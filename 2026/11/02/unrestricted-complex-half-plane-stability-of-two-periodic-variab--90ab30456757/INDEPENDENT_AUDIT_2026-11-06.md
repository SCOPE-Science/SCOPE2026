# Independent mathematical audit

## correctness

PASS

For standard variable-step BDF2 on exactly alternating steps h,rh, the two-step companion matrix has determinant 1/D and trace N/D, D=z^2+(chi+4)z+2chi+5, N=2chi+6-chi*z and chi=r+1/r. The complex quadratic Schur-Cohn test reduces to |D|>1 and |N conjugate(D)-conjugate(N)|<|D|^2-1. For Re z=x>=0, Q=|z|^2>0 and chi>=2, the explicit identity ((|D|^2-1)^2-|N conjugate(D)-conjugate(N)|^2)=F G with F=Q^2+2(chi+4)xQ+4(2chi+5)x^2+8(chi+2)x>0 and G=F+(chi+2)(chi+6)Q+12(chi+2)^2 x+4(chi+2)^2(chi+3)>0 proves both multipliers strictly inside the disk. At z=0 they are distinct 1 and 1/(2chi+5); fixed-r stiff limit is zero; r->infty roots become 0 and (2-z)/(2+z). Symbolic factor verification and direct complex roots were independently replayed; sampled roots cannot replace the strict all-half-plane positivity.

## originality

PASS

General-grid BDF2 ratio restrictions and small-step perturbation stability do not imply a two-period scalar A-stability inequality for arbitrary positive ratio and all complex z in a half-plane. The period-two Floquet product and singular CN limit do not follow from constant-step BDF2 A-stability. Li-Liao full primary PDF was examined for its small-max-step Theorem 2.1; Bourgault-Garon deferred-correction full text remains inaccessible, with abstract-only A-stability claims possibly relevant but algorithm and constraints not established as equivalent. This is a qualified best-of-knowledge decision rather than categorical noncoverage.

## value

PASS

Exact complex half-plane Floquet stability for any fixed alternating ratio is a nontrivial exception to restrictions common in general variable-step BDF2 analyses. The singular Crank-Nicolson limit shows precisely why strict pointwise damping is not a ratio-uniform imaginary-axis damping estimate. This sharp analytic boundary may inform stability of strongly alternating adaptive integrations without claiming nonlinear or arbitrary-grid stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
