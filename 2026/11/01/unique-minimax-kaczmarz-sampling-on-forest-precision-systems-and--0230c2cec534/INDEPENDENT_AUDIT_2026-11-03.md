# Independent mathematical audit

## correctness

PASS

For unit Euclidean rows of invertible real square B, one row projection subtracts |b_i^T z|², giving exactly gamma(p)=lambda_min(B^T diag(p)B) as the worst-direction conditional one-step expected squared decrement. PSD congruence yields diag(p)-lambda K >=0, K=(BB^T)^(-1). A sign vector s on each forest component with s_i s_j=sign(K_ij) gives 1>=lambda T, T=tr K+2 sum_{i<j}|K_ij|. With d_i=K_ii+sum_{j!=i}|K_ij|, diag(d)-K is a sum of positive rank-one signed edge Laplacians, proving p*=d/T achieves gamma=1/T. At optimality a PSD zero quadratic form forces (diag(p)-K/T)s=0, which uniquely determines all coordinates; includes zero edges, isolated vertices and disconnected forest. Gaussian edge autoregression directly yields G_ij=product path rho_e and inverse precision K_ii=1+sum rho_e²/(1-rho_e²), K_ij=-rho_e/(1-rho_e²) on edges; thus p_i=(1+sum incident |rho_e|/(1-|rho_e|))/[N+2 sum_e |rho_e|/(1-|rho_e|)]. Equal magnitude r yields p_i=(1-r+r degree_i)/(N+(N-2)r) and gamma=(1-r)/(N+(N-2)r), independent tree topology. No cyclic or rectangular extension is proven.

## originality

PASS

Forest-precision exact unique optimizer and tree topology-invariant rate are additional structural results beyond norm-based randomized Kaczmarz and previously formulated general probability-selection SDPs. Dai et al and Gower–Richtárik give the same one-step eigenvalue/SDP objective but not an inspected explicit forest formula. The complete accessible Agaskar–Wang–Lu (2014) paper instead optimizes annealed long-run mean-square decay using a tensor-square propagator; it does not state a sharp forest-precision one-step optimizer. This qualified decision does not claim that negative searches prove worldwide novelty.

## value

PASS

The closed global optimizer is a complete, natural structural solution to a nontrivial convex design problem over an infinite class of Gaussian graphical linear systems, with global uniqueness and the surprisingly topology-independent optimal rate at fixed edge magnitude. It is not a renaming of the general SDP and it distinguishes topology-dependent probabilities from topology-independent rate. This exact minimax one-step contraction could guide choice of row sampling for tree-structured precision systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
