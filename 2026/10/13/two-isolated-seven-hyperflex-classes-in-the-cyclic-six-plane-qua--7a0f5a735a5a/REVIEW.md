# Independent mathematical audit

## correctness

PASS

Reconstructed the full geometric census over C by tangent contact, independently of the uploaded Hessian checker. In the affine chart with x nonzero, put f(y)=y^4+r y^2+1 and solve x^3=-f(y) for x as a function of the local coordinate y. Differentiating gives 9 f(y)^2 x''(y)/x(y)=3 f(y) f''(y)-2 f'(y)^2=2P_r(y^2). The order of vanishing of x'' is the tangent contact order minus two in characteristic zero. For a root t of g_r(t)=t^2+rt+1 the remainder is P_r(t)=-4t(2t+r)^2, nonzero since r^2 is not 4 and g_r(0)=1. Also P_r(0)=3r is nonzero on the stated domain. Thus every root t of the cubic gives six distinct points with nonzero x,y, on which y^2-t is a uniformizer. These are a free C6 orbit; simple and double roots give ordinary flexes and hyperflexes respectively. The independent exact tangent/discriminant computation (replay: /workspace/branches/record-5-independent.py) gave the discriminant 3(r^2-4)(11r^4-1080r^2+3888); matching coefficients of a triple root would simultaneously require r^2=108/31 and r^2=324/125. The four distinct affine points with x=0 are smooth with horizontal tangent y=y_0 of contact three. At the only point at infinity [1:0:0], F_Z=1 and the tangent Z=0 has contact four. These cases exhaust the smooth quartic and give distinct-point profiles (one hyperflex, 22 ordinary flexes) and (seven hyperflexes, ten ordinary flexes), each of weighted degree 24. The quadratic in u=r^2 has the two distinct admissible roots (540 +/- 288 sqrt(3))/11. The unmarked-curve isomorphism criterion in Theorem A of Ohashi–Kudo–Harashita identifies r and -r but not curves with the two different squared parameters. Isolation is relative to the full-C6 moduli line, not the full genus-three moduli space. The frozen checker was read, not executed.

## originality

PASS

The supported contribution is the exact intersection with the full-C6 line and the distinct-point flex profile there, including the single six-point orbit. The normal form, isomorphism parameter, Hessian criterion and global seven-hyperflex strata are prior. Comparison identified both real overlap with the Vermeulen classification and a later positive-characteristic analogue, not verified prior coverage of the characteristic-zero intersection and census.

## value

PASS

The C6 locus and flex profile are intrinsic, independently motivated moduli data. The two exact intersection points and their ordinary/hyperflex orbit census distinguish special stable configurations from the generic one-hyperflex case, as needed for comparing the automorphism and hyperflex stratifications. This is a useful exact intersection in a known global locus, not a claim to discover the ambient seven-hyperflex locus or merely to recompute its table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
