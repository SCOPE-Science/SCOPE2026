# Independent mathematical audit

## correctness

PASS

Writing f=f(root)1+Σ_{v!=root}(f(v)-f(parent v))1_{T_v} identifies edge variation with ℓ1 increment coordinates, hence norm equals largest column V(A1_{T_v}). For t=s_v, g on strict ancestors a is t/s_a; path telescopes 1-t/N while each off-path branch edge contributes t/s_a, giving exact formula. Any nonpath contains degree>=3, producing an ancestor contribution larger than 1/N for a suitable child, whereas paths yield columns ≤1. If S_i denotes sizes along ancestor chain, (b_i-1)<=S_i-S_{i+1}-1 and Σ(S_i-S_{i+1})/S_i<=log(N/t), so norm≤1+N/e. Distributing N−t−sqrt(N) leaves evenly over sqrt(N) ancestor spine vertices ending in t≈N/e subtree yields ≥N/e−O(sqrt N), proving the limit. Independently computed 119 rational direct subtree indicator columns and confirmed formula; read verifier source. No claim of exact finite-N maximum.

## originality

PASS

Best-of-knowledge originality survives the actual implication comparisons; cited antecedents cover the foundations or narrower/different objects but none of the accessible material establishes this exact completed statement. Uninspected plausible literature is explicitly treated as residual priority risk, not a proven absence.

## value

PASS

Natural averaging operator preserves positivity/constants yet can amplify edge variation linearly; exact seminorm, path-only contractivity and 1/e sharp coefficient form a motivated structural/extremal theorem useful for hierarchical smoothing and BV analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
