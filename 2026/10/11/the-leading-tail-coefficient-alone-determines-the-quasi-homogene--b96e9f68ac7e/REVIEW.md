# Independent mathematical audit

## correctness

PASS

Starting from the stated closed formula C=a(A(r)-B(r)log r), where a=min(k,l), r=max(k,l)/a>1, A=r(r+1)/(r-1)^2 and B=2r²/(r-1)^3, equality of two coefficients yields q=αlog r−βlog s with q,α,β rational and α,β positive. Multiplication by a common denominator gives integer Q=m log r−n log s, so e^Q=r^m/s^n is rational. Hermite–Lindemann forbids any nonzero integer Q; thus q=0 and the rational and logarithmic parts agree separately. Their quotient gives h(log r)=h(log s) with h(x)=x/sinh x, strictly decreasing on x>0, hence r=s, then a=c and b=d. Independent algebra confirmed B/A=1/sinh(log r) and representative coefficient integrals. Finite high-precision stress testing is not used as infinite proof. The conclusion is exact, not stable numerical inversion.

## originality

PASS

The focal Liu–Lu–Yang abstract gives recovery from first strict descent PLUS asymptotic leading coefficient, while their companion full-invariant work recovers parameters from the entire sequence. A theorem that two statistics recover parameters does not imply injectivity of either statistic individually; this proof uses an additional transcendence separation and monotonicity. Public full text of the recent preprints could not be inspected owing to access failures; the precise Remark 3.3 attribution is retained as unverified manuscript evidence and overlap remains material. Nothing inspected decisively implies single-leading-coefficient recovery.

## value

PASS

Reducing a natural analytic classification from two distinct asymptotic statistics to a single leading tail coefficient is a mathematically motivated minimal-data rigidity result, not a numerical scan. The proof uncovers a nontrivial arithmetic independence of rational and logarithmic portions. This exact-identifiability theorem does not imply robust reconstruction from noisy finite-precision coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
