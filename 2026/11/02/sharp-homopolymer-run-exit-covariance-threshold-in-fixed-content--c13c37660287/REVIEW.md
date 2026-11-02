# Scientific review: fixed-content triple-pattern covariance

## Correctness — PASS

For a uniform binary word with fixed zero count \(a\) and one count \(b\), each prescribed collection of sites has the exact falling-factorial probability. The compatible \(000\)/\(001\) overlap shifts are \(+1\) and \(+2\), and all farther windows have disjoint support. Their first and mixed moments give the rational covariance in `RESULT.md`. The factorized numerator establishes the threshold, while modular reduction forces the only nondegenerate equality cases \((n,a,b)=(4,3,1)\) and \((9,4,5)\). Independent exact enumeration and placement checks completed 79,723 assertions. The universal statement rests on the algebraic proof, not on the enumeration.

## Originality — PASS, with stated priority risks

Rukhin's 2010 full text supplies Markov/independent word-frequency methods, while Régnier's 2000 work supplies exact occurrence moments for Bernoulli and Markov text. Both differ from the fixed-count sampling-without-replacement model. The closest inspected fixed-composition dependence result treats pairwise two-site transition indicators, not the \(000\) and \(001\) count covariance or its linear-in-\(a\) sign boundary. Exact query phrases and scientific implication comparisons are recorded in `AUDIT.json`. General word-enumerator work may encode this computation implicitly, and exhaustive historical priority review has not been achieved.

## Mathematical value — PASS

Two natural zero-run profile statistics respond differently to fixed zero frequency: excess length beyond two in every zero run and the number of zero runs of length at least two that exit into a one. Their covariance changes from positive to negative at an exact finite-sample threshold. An arithmetic argument identifies exactly two nondegenerate zero-covariance compositions across all sizes. This is a complete second-order sign classification for the specified motif pair and is relevant to covariance calibration in fixed-content word-pattern tests. No independence, test-power or higher-order claim is made.

Self-review: passed. Independent audit: not yet performed.
