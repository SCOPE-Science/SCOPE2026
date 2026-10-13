# Ceiling threshold for prime-power multiplicative monoid morphisms
## Finding
In the nonconstant family of multiplicative monoid morphisms parameterized in arXiv:2610.02393v1, the valuation parameter must satisfy
\[
ev\ge f,
\]
and therefore the correct lower bound is
\[
v\ge \left\lceil\frac{f}{e}\right\rceil,
\]
not \(v\ge\left\lfloor f/e\right\rfloor\). With the other compatibility hypotheses of the source left unchanged, replacing the printed floor by the ceiling repairs the valuation step in Proposition 3.1 and the corresponding lower limits in Definition-Lemma 3.3 and Theorem 3.4.

Consequently, whenever \(f>e\) and \(e\nmid f\), the printed bottom stratum \(v=\left\lfloor f/e\right\rfloor\) is spurious. In the smallest odd-prime witness
\[
p=q=3,\qquad e=2,\qquad f=3,
\]
the printed parameter model gives \(55\) maps, while the corrected model and an exhaustive multiplication-table enumeration both give exactly \(19\) unital multiplicative monoid homomorphisms from \(\mathbb Z/9\mathbb Z\) to \(\mathbb Z/27\mathbb Z\).

## Assumptions and scope
Let \(p,q\) be primes and let \(e,f\ge1\). The source writes a nonconstant map in the form
\[
\psi_{r,\varphi,v}\bigl([p]^u[b]\bigr)
 =[q]^{uv}[r]^u\varphi([b]),
\]
where the displayed unit factors are invertible in the target and the remaining source hypotheses impose the stated unit-group compatibility conditions. Monoid homomorphisms are unital.

This finding concerns the lower valuation threshold in version 1 of arXiv:2610.02393. It does not alter cases in which \(e\mid f\) or \(f\le e\), because there the relevant floor and ceiling either agree or the lower bound is already \(1\). It also does not reassess unrelated structural assertions of the paper.

## Proof
The zero element of the source monoid is represented by \([p]^e\). For a purported nonconstant map of the displayed form, well-definedness at zero requires
\[
0=\psi([p]^e)=[q]^{ev}[r]^e.
\]
The factor \([r]^e\) is a unit. Hence the right-hand side vanishes modulo \(q^f\) if and only if
\[
ev\ge f.
\]
Since \(v\) is an integer, this is equivalent to
\[
v\ge \left\lceil\frac{f}{e}\right\rceil.
\]
The implication printed in the source, from \(ev\ge f\) to \(v\ge\lfloor f/e\rfloor\), is true but too weak to characterize the allowed integers. If \(f>e\) and \(e\nmid f\), then
\[
e\left\lfloor\frac{f}{e}\right\rfloor<f,
\]
so the entire printed bottom stratum fails the zero test.

For the concrete choice \(p=q=3\), \(e=2\), and \(f=3\), the printed lower bound allows \(v=1\). Taking \(r=1\) and the trivial unit homomorphism gives
\[
\psi(0)=\psi([3]^2)=[3]^2=[9]\ne[0]\pmod{27},
\]
so this purported map is not well-defined as a monoid homomorphism.

The source's own cardinality model makes the numerical effect explicit. Here the unit-group homomorphism factor has size
\[
\gcd\bigl(\varphi(9),\varphi(27)\bigr)=\gcd(6,18)=6.
\]
The printed values \(v=1,2,3\) therefore contribute
\[
6\bigl(|U_9|+|U_3|+|U_1|\bigr)=6(6+2+1)=54
\]
nonconstant parameters, and the special constant-one morphism raises the printed total to \(55\). The corrected lower bound allows only \(v=2,3\), giving
\[
1+6(2+1)=19.
\]

With the ceiling bound imposed, the later valuation argument in the source has the needed inequality \(uv\ge ev\ge f\) whenever \(u\ge e\); the other well-definedness comparisons continue to use the source's unit-group compatibility condition. Thus the correction is precisely a lower-bound repair, not a replacement of the rest of the parametrization.

## Verification
The standalone program `verify.py` independently enumerates all candidates from the images of the multiplicative generators \(2\) and \(3\) of \(\mathbb Z/9\mathbb Z\), constructs their values on all nine residues, and checks the homomorphism identity on all \(81\) ordered products. It finds exactly \(19\) distinct unital multiplicative maps. It also computes the printed parameter count \(55\), the corrected count \(19\), and checks that the forbidden \(v=1\) formula sends zero to \(9\) modulo \(27\). Running the supplied file produces `verification.txt` ending in `VERIFY_OK`.

The finite enumeration verifies the concrete \(9\)-to-\(27\) count only. The general ceiling threshold is proved symbolically by the zero-element valuation argument above.

## Relationship to prior work
The motivating preprint, arXiv:2610.02393v1, states the classification with the floor lower bound in Proposition 3.1, Definition-Lemma 3.3, and Theorem 3.4. Its proof itself derives the stronger necessary condition \(ev\ge f\), which yields the ceiling bound.

The earlier paper arXiv:2408.06278v2 studies automorphisms of the multiplicative monoid modulo a single prime power. It does not treat the unequal source-target exponent comparison responsible for the floor-versus-ceiling discrepancy here.

Checked published-result records and targeted literature searches did not locate an equivalent correction or the exact \(19\)-map witness. The closest located results concern other prime-power congruence or monoid phenomena and do not imply this statement.

## Limitations
The correction is asserted for arXiv:2610.02393v1, first public on 1 October 2026. A later revision may incorporate the same repair. The exact count \(19\) is established only for the explicit witness \(\mathbb Z/9\mathbb Z\to\mathbb Z/27\mathbb Z\); no new closed count formula beyond the source's parametrization with the corrected lower limit is claimed.

The exhaustive program is not an infinite proof. It is an independent finite check of the smallest odd-prime witness and of the numerical consequence of the corrected threshold.

## References
1. J. Atalaye, L. Baker, and S. Marques, “Prime-Power Multiplicative Modular Monoid Morphisms,” arXiv:2610.02393v1, first submitted 1 October 2026.
2. J. Atalaye, L. Baker, and S. Marques, “On the automorphism group of the monoid of the integers modulo a prime power,” arXiv:2408.06278v2.
