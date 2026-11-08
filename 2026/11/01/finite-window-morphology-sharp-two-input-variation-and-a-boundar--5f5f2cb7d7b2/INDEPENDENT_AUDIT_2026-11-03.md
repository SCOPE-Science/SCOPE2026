# Independent mathematical audit

## correctness

PASS

For each n>=2 and integer 0<=r<=n-1, each generic truncated sliding min/max is an ordered coordinate selector p_1<=...<=p_n. Its linearization sends disjoint input edge intervals [p_i,p_(i+1)-1] to separate output jumps, giving exact weighted norm max w_i/w_k over realized crossings. Equal neighboring windows force inactive edges i<=r and i+r>=n; every permitted crossing with max(1,i-r)<=k<=min(n-1,i+r) is realized by a strictly ordered input selecting an exiting left or entering right endpoint, followed by an arbitrarily small step perturbation. Piecewise-affine integration along segments proves sharp global two-input bound. For 1<=r<=n-2, connectivity of active pairs forces equal active weights c and inactive weights >=c; uniform coefficient is 1 except r=n-1 where it is 0; arbitrary unweighted compositions contract. Boundary n=2 and r=0 included.

## originality

PASS

Single-input LULU total-variation decrease and residual preservation are prior facts; they do not imply a two-input variation Lipschitz bound. Exact positive-weight coefficient and near-global inactive-boundary-band classification are not established in the inspected 2007 Anguelov–Rohwer material or the accessible 2002 abstract. The directly relevant older 2002 journal article / 2005 monograph could contain an equivalent result; authorized full text remained inaccessible and Oxford retrieval was safety-blocked, so this remains named priority risk and is not automatically scientific failure.

## value

PASS

Nonlinear erosion/dilation sensitivity to changes between two inputs is a natural robustness question distinct from smoothing one input. Complete exact sharp weighted operator norms and the nonuniform boundary-weight transition give an explicit criterion for robust edge weighting and explain unweighted contractivity of cascades.

The dated certificate retains the supplied scientific assessment, sources and limitations.
