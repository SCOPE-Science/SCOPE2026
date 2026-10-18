# Independent mathematical audit

## correctness

PASS

The primary weighted-Gram spectrum on the face w3=0 reduces entropy to H(w0,w1,w2)+w1 log(4N)+w2 log(3N), with m=w1+2w2 and N=exp(h(t²/(1+t²))). Gibbs variational inequality at r=m/(4-m) bounds the objective by log[(1+4Nr+3Nr²)/(1+r)^4]. Its derivative has sign 4(N-1)-6Nr-6Nr², with unique r>0 solving r(1+r)=2(N-1)/(3N), and Gibbs weights at that r satisfy m=4r/(1+r); equality is feasible and unique. Independent symbolic expansion of log Bhat at s=log N found 4s²/3−56s³/27+O(s⁴), yielding 16/3*t^4 log²(1/t); numerical check t=1 Bhat≈1.382955. The exact face implies only Bfull≥Bhat and exponent lower bound by the source theorem; it does NOT show global optimum.

## originality

PASS

Wei–Wu–Liu–Liu arXiv:2610.02172 states the full implicit variational exponent, qualitative 1<B_t≤N_t, and a smaller one-dimensional witness. Actual relevant full text supplies no closed optimized w3=0 face, unique Gibbs weights, or coefficient 4/3 for its near-Gaussian collapse. Cudby–Strelchuk earlier Gaussian-rank work treats different finite-copy/simulation invariants. Targeted published Resultary semantic search found no equivalent same-object theorem.

## value

PASS

Turns an implicit optimization and qualitative exponential growth into a fully explicit parameter-dependent lower exponent and sharp small-nonGaussianity collapse law, with a structurally natural identifiable Gram face. Researchers can use this exact certificate without solving the full three-variable entropy program; carefully limited to lower bound rather than equality with full base.

The dated certificate retains the supplied scientific assessment, sources and limitations.
