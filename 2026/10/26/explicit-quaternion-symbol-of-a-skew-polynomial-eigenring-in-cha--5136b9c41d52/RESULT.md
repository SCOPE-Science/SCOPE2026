# Explicit quaternion symbol of a skew-polynomial eigenring in characteristic two

## Finding

For every odd integer \(r\ge3\), let \(L=\mathbb F_{2^r}(t)\), \(K=\mathbb F_2(s)\), where \(s=t+t^{-1}\). Let \(\tau\) square constants in \(\mathbb F_{2^r}\) and fix \(t\), let \(\theta(t)=t^{-1}\) and let \(\theta\) fix constants, and put \(\sigma=\tau\theta\). In the skew-polynomial ring \(R=L[x;\sigma]\), defined by \(xa=\sigma(a)x\), set
\[
f=x^2+\frac{t^2+1}{t^2+t+1}=x^2+\frac{s}{s+1}.
\]
The eigenring \(\mathcal E(f)\) is \(K\)-isomorphic to the characteristic-two quaternion division algebra
\[
\boxed{\left[\frac1s,\frac{s}{s+1}\right)_K}.
\]
Here \([a,b)_K\) denotes the algebra generated over \(K\) by \(i,j\) with \(i^2+i=a\), \(j^2=b\), and \(ji=(i+1)j\). Thus the precise Brauer class of this right-nucleus algebra is specified, not just its degree.

## Assumptions and scope

The integer \(r\) is odd and at least three. All fields have characteristic two; \(s\) is transcendental over \(\mathbb F_2\), and \(K=\mathbb F_2(s)\). The automorphisms commute, \(\sigma\) has order \(2r\), and \(\operatorname{Fix}(\sigma^2)=\mathbb F_2(t)\). The polynomial \(f\) is the irreducible skew polynomial from Proposition 3.2 of Lobillo–Santonastaso–Sheekey. The eigenring is \(\mathcal E(f)=I(f)/Rf\), where \(I(f)=\{g\in R:fg\in Rf\}\). No claim is made about arbitrary skew polynomials, arbitrary central division algebras, or a full isotopy classification of the surrounding semifield families.

## Proof

First, \(s=(t^2+1)/t\), so \(t^2+st+1=0\). It follows that
\[
\frac{t^2+1}{t^2+t+1}=\frac{st}{t(s+1)}=\frac{s}{s+1}=:c\in K,
\]
and hence \(\sigma(c)=c\). Because \(r\) is odd, \(\operatorname{Fix}(\sigma^2)=\operatorname{Fix}(\tau^2)=\mathbb F_2(t)\). The cited source proves that \(f=x^2+c\) is irreducible: a hypothetical factorization forces a rational-function norm equation with denominator factor \(t^2+t+1\); the denominator-divisibility argument forces that irreducible factor to divide both coprime numerator and denominator. Its Theorem 2.6 then gives that \(\mathcal E(f)\) is a central division algebra of degree two over \(K\).

Every residue class modulo the degree-two polynomial \(f\) has a representative \(g=a+bx\), with \(a,b\in L\). Expanding with \(xa=\sigma(a)x\) gives
\[
fg=\sigma^2(b)x^3+\sigma^2(a)x^2+cbx+ca.
\]
Writing \(fg=(u+vx)f\) and comparing coefficients gives \(u=\sigma^2(a)\), \(v=\sigma^2(b)\), \(ca=\sigma^2(a)c\), and \(cb=\sigma^2(b)\sigma(c)\). Since \(c\) is central in \(L\) and \(\sigma(c)=c\), these equations are equivalent to \(a,b\in\operatorname{Fix}(\sigma^2)=\mathbb F_2(t)\). Conversely, every such pair satisfies them. Therefore
\[
\mathcal E(f)=\mathbb F_2(t)\oplus\mathbb F_2(t)x,
\]
with \(x^2=c\) and \(xa=\theta(a)x\) for \(a\in\mathbb F_2(t)\).

Put \(i=t/s+1/s\) and \(j=x\). The relation \(t^2+st+1=0\) gives \(i^2+i=1/s\). Also \(j^2=c=s/(s+1)\), and \(t^{-1}=t+s\) gives \(\theta(i)=i+1\), hence \(ji=(i+1)j\). These are exactly the defining relations of \([1/s,s/(s+1))_K\), and both algebras have dimension four over \(K\), proving the isomorphism.

For completeness, the displayed quaternion algebra is division independently of the degree statement. The extension \(E=\mathbb F_2(t)/K\) is quadratic with polynomial \(T^2+sT+1\). At the prime \(\mathfrak p=(s+1)\), the reduction is \(T^2+T+1\), irreducible over \(\mathbb F_2\), and the derivative is nonzero there; thus \(\mathfrak p\) is inert and unramified of residue degree two. Norms from \(E/K\) therefore have even valuation at \(\mathfrak p\), while \(c=s/(s+1)\) has valuation \(-1\). So \(c\) is not a norm. The quadratic cyclic algebra \((E/K,\theta,c)\), equivalently the displayed quaternion symbol, is nonsplit and hence division.

## Verification

The algebraic checks are explicit: \(c=s/(s+1)\); \(\operatorname{Fix}(\sigma^2)=\mathbb F_2(t)\); the coefficient comparison characterizes the eigenring; and the generators \(i,j\) satisfy all three quaternion relations. The inert-prime valuation proves the division property without relying on a finite computation. The source's Proposition 3.2 and Theorem 2.6 were read in the full article and used only for irreducibility of the specified \(f\) and the stated eigenring context; the explicit symbol presentation is derived here from the defining relations.

## Relationship to prior work

Lobillo, Santonastaso, and Sheekey construct this skew-polynomial example and establish that its eigenring is a central division algebra of degree two; their later Theorem 5.17 uses the eigenring to compare isotopy types. The paper does not state the symbol \([1/s,s/(s+1))_K\) for this eigenring. The present calculation identifies the Brauer class explicitly. The nearby indexed result on root-linear maps for characteristic-two quaternion division algebras concerns a different field and a different invariant, not this eigenring. This is a bounded comparison, not an absolute priority claim.

## Limitations

The presentation is for the single explicit family and for odd \(r\ge3\). It does not classify all degree-two division algebras over \(\mathbb F_2(s)\), nor does it solve the separate equal-parameter isotopy problem noted in Remark 6.8 for a finite-field family. An earlier explicit computation of the same symbol in the cited eigenring literature remains a residual priority risk and should be checked by independent review.

## References

1. F. J. Lobillo, P. Santonastaso, and J. Sheekey, “Quotients of skew polynomial rings: new constructions of division algebras and MRD codes,” arXiv:2502.13531v1 (first public version 2025-02-19), especially §2.2, Proposition 3.2, Theorem 2.6, §3.1, and Theorem 5.17. https://arxiv.org/abs/2502.13531
2. Standard cyclic-algebra norm criterion: for a cyclic quadratic extension \(E/K\), the cyclic algebra \((E/K,\theta,c)\) is split exactly when \(c\in N_{E/K}(E^\times)\).
