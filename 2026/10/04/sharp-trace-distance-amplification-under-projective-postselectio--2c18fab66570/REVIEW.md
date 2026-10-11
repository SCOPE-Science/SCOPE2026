# Independent mathematical audit

## correctness

PASS

Pinching into accepted/rejected blocks cannot increase trace distance. Each block contributes at least half the acceptance-probability gap by its trace, while for \(p\ge q\) the accepted block also satisfies \(\delta_P\ge pc-|p-q|/2\) by the triangle inequality. Adding the rejected-block contribution yields exactly \(\max\{|p-q|,pc\}\); swapping states handles \(q\ge p\). The three-outcome diagonal family has conditional distance \(c_*=\min(1,\tau/p)\) and input distance \(\max(p-q,pc_*)\le\tau\), proving sharpness. A fresh independent random-matrix check verified the inequality on 100 noncommuting instances. The relationship paragraph in RESULT.md contains one pre-existing unmatched LaTeX brace in its display of the weaker source bound; the theorem and proof are unaffected.

## originality

PASS

The defining recent MERA-certification paper advertises inverse-acceptance amplification under normalized postselection and, according to the frozen source comparison, gives a weaker acceptance-resolved bound with an additional half acceptance-gap term. Its full text could not be materially obtained through open routes in this run, and the authorized institutional retrieval attempt returned an unavailable/invalid-worker error, so exact theorem-level overlap remains a specific residual risk. Gavorová and Shi–Waks study broader postselected/non-trace-preserving map metrics, but the inspected statements are operation-level or constant-factor bounds rather than this state-pair exact envelope. Resultary search found no covering theorem.

## value

PASS

Postselection is intrinsically nonlinear after renormalization, and exact perturbation amplification is directly relevant to finite-measurement certification. The theorem gives the optimal acceptance-resolved one-step constant for arbitrary unequal success probabilities, with sharp witnesses, improving the accessible prior inverse-acceptance picture rather than merely demonstrating instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
