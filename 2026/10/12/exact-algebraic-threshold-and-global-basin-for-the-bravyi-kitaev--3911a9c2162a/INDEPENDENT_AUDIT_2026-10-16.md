# Independent mathematical audit

## correctness

PASS

Frozen RESULT.md e480171b22c1a702b3a73e910f49a3c79dc98d39 reproduces Bravyi--Kitaev Eq(36) rational recurrence with r=1−2ε. Independently sympy-expanded f−ε = r(1−r²)Q(r²)/(2(1+15r^8)) and reciprocal identity Q(y)/y³=q(y+1/y), q(z)=z³+z²−2z−16, yielding exactly one positive physical root z*=2.459120158... since q(2)<0, q(3)>0 and q′>0 for z≥2. Direction of Q signs proves f<ε below ε*, f>ε above it; AM≥GM establishes f≥0, while f≤1/2 is immediate. Continuous monotone bounded iteration converges to fixed points; endpoints included separately. This is restricted to conditional, ideal postselected protocol; no fidelity claim for non-postselected stochastic rounds.

## originality

PASS

The original Bravyi--Kitaev paper derives exactly this rational map and prints only ε0≈0.141 numerically; independent exact polynomial/cubic closed form and global basin sign proof are not stated there. Later magic distillation improvements modify protocols rather than imply the identical 15-to-1 map root algebra or monotone global attraction.

## value

PASS

The H-state 15-to-1 recurrence is a canonical quantum error-distillation map. Knowing a unique exact algebraic threshold and full basin characterizes its deterministic conditional iteration without relying on numerical root selection, and gives precise boundary behavior for calibration. This is motivated exact dynamics of a standard protocol, not an arbitrary algebraic root.

The dated certificate retains the supplied scientific assessment, sources and limitations.
