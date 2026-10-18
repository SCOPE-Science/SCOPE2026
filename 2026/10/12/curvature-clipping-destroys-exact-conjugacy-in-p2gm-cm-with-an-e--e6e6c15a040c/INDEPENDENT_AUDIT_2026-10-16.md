# Independent mathematical audit

## correctness

PASS

On an SPD quadratic H(v)=Hv. Substitution gives the defect identity exactly. For H=diag(1,1/2), x0=(1,1), gradient step v0=(-1,-1/2) satisfies Armijo sigma=1/2 because f(x1)-f(x0)=-11/16<-5/8. At x1=(0,1/2), v1=(0,-1/4), r=1/2, q=1/4, s^THv=1/16, the projection coefficient is 4 and the Hessian cross term is -1/16. For cap tau↓0 the exact H cosine approaches -1. Independent rational arithmetic and source verifier inspection confirm; repair is algebraic only, NOT a convergence guarantee.

## originality

PASS

Source-specific exact projection defect and source-compliant accepted-step counterexample extend beyond source separate exact theoretical subspace and clipped practical algorithm; no directly covering defect law found in published corpus. Best-of-knowledge original, no claim of disproving convergence.

## value

PASS

Conjugacy is used to diagonalize the 2D quadratic subspace in the motivating method. Implementation clipping can cause near maximal nonorthogonality on a real accepted trajectory, while separating clipped model weights from unclipped orthogonalization is a mathematically precise repair; the structural issue is not an unmotivated normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
