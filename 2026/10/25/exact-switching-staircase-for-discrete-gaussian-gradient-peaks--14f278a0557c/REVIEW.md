# Independent mathematical audit

## correctness

PASS

For all n>=0, x>0 use r=I_{n+1}(x)/I_n(x), a=n+1, q=x/(x+a); the Bessel recurrence gives H_n=2I_n[1-(1+a/x)r], hence sign H_n=-sign(r-q). Riccati r'=1-(2a-1)r/x-r² yields at each contact (r-q)'=(x-a²)/(x+a)². The near-zero series makes r-q<0; contact at x=a² has positive second derivative, so no first contact at or below a². Above a² every zero is an upward transversal crossing, hence at most one. The known Amos-type lower barrier L=x/(a-1/2+sqrt(x²+(a+1/2)²)) satisfies a strict differential subsolution inequality and r-L>0 for x small; at x=a(a+1), L=q, forcing the unique root in (a²,a(a+1)). This gives positive-to-negative sign and disjoint root brackets. b_n=I_n-I_{n+1}>0 and H_n=b_n-b_{n+1}, yielding unique unimodal discrete maximizer between consecutive switches and a two-way adjacent tie only at switches. Discrete heat kernel exp(-2t)I_|k|(2t) makes the ℓ¹→ℓ∞ convolution norm the largest absolute kernel difference. Independent symbolic checks reproduce Riccati contact and lower-barrier small-x coefficient; independent high-precision roots for n=0..12 lie in open intervals with correct signs.

## originality

PASS

First and second modified-Bessel differences and Amos ratio bounds are classical and explicitly acknowledged. The all-n single-root classification with quadratic brackets, unique peak-index staircase and sharp gradient norm transitions is a separate theorem not established by the inspected references.

## value

PASS

The exact location and unique order of every optimizer switch is a natural sharp norm profile of the one-dimensional lattice heat semigroup, rather than a cosmetic Bessel bound. Strict all-n brackets identify discrete scale transitions in terms of quadratic mode indices, potentially useful in optimal gradient estimates and extremizer geometry. Value is the full sharp staircase, not the classical ratio estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
