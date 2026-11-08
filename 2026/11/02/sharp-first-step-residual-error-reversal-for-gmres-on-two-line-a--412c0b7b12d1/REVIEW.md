# Independent mathematical audit

## correctness

PASS

For 0<c<1 and z=c², multiplying P2P1 gives T=[[z,0],[cs,0]]. The Euclidean GMRES(1) normal equation gives step α=1/(1+z−z²) and exact squared ratios residual 1/(1+z−z²)<1 versus AP, solution error 1+z(1−z)^3/(1+z−z²)^2>1. Independently factored derivative (1−z)^2(z²−5z+1)/(1+z−z²)^3, confirming unique sharp z=(5−sqrt21)/2 and 1.037386... error penalty; nonzero det(Ax0,A²x0)=−cs³ gives two-step exact solve while repeated AP remains nonzero. All real 0<z<1 analytically covered; rational checker examined but not executed as a source program.

## originality

PASS

Exact two-line first-step cross-algorithm metric comparison and optimized 1.037386 constant not found in inspected affine Anderson, classical GMRES or other published nearby results; prior generic residual/error mismatch and 2x2 formulas are credited. Bounded priority risk remains.

## value

PASS

A motivated finite-horizon algorithm comparison isolates a genuine residual-versus-solution metric reversal in the simplest nonnormal projection product, proves its all-angle sharp constant, and contrasts one-step harm with two-step termination. The penalty is small (~3.74%) but is a precise diagnostic rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
