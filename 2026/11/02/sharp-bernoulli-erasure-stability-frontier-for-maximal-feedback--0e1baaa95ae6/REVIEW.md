# Independent mathematical audit

## correctness

PASS

The algorithm update under B=0 and B=1 gives A0=[[1,0,-gamma],[1,1,-1],[0,0,1]], A1=[[1-gamma,-gamma,0],[0,0,0],[1,1,0]]. On symmetric second moments the 6x6 map satisfies det(I-M)=gamma*q^2*((q-1)*gamma^2+(7q-8)*gamma+6q-4), checked independently by symbolic algebra. For q>2/3 the displayed positive-definite P solves internal Lyapunov equation at gamma=0; the unique slow moment eigenvalue has derivative -2; PSD cone continuity and positive eigenvalue prevent a hidden crossing before gamma_*(q). The negative determinant outside the root forces real spectral eigenvalue >1. For 0<q<1, A0 has a single length-three unipotent Jordan chain and A1 breaks both proper invariant subspaces, ensuring positive-definite adjoint Perron eigenmatrix, then primal-square identity forces auxiliary decay if primal decays, contradiction. q=1 reduces to ordinary gradient descent after finite transients. Direct symbolic determinant, Lyapunov, and sampled spectral tests corroborate, not replace proof.

## originality

PASS

Gao–Islamov–Stich introduced the precise algorithm and note difficulties with full feedback for different Top-1 examples. Their regulated-eta convergence results do not imply the necessary-and-sufficient eta=1 Bernoulli q and gamma curve. Classical Bernoulli error-feedback has a different two-state delay law and allows small steps for every q>0, and EF21 employs another memory. The model-specific exact three-state phase transition appears distinct, with residual specialized-priority risk.

## value

PASS

A sharp reliability threshold q=2/3 below which arbitrarily small positive steps provably fail is a meaningful algorithmic obstruction, not a routine rate improvement. The exact optimal stability region clarifies when maximal feedback requires qualitative regulation, while remaining restricted to this natural scalar test model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
