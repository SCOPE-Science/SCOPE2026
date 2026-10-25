# Independent mathematical audit

## correctness

PASS

For each fixed radius the complete sliding-window average of a valley sequence is valley-shaped because the increment is f[x+r+1]-f[x-r], which changes sign from negative to positive at most once. The proof treats truncated graph balls: a left-truncated ball at middle center j is reproducible as a centered ball from any earlier i, and similarly right clipping from later k, proving global quasiconvexity Mf(j)<=max(Mf(i),Mf(k)) for i<j<k. Endpoint prefix and suffix means are themselves valley-shaped sequences, hence Mf(0)=max(f0,mu) and Mf(n-1)=max(f(n-1),mu); every vertex permits full mean mu. Therefore Var(Mf)<= (A-t)_++(B-t)_+, where A=f0-h, B=f(n-1)-h, t=mu-h >=(A+B)/n. The algebra gives coefficient (1-1/n), explicit sharp deficit [min((n-1)A,B)+min((n-1)B,A)]/n; equality only constant-baseline one-endpoint spike, with two equal endpoint spikes attaining the deficit. Domain arbitrary n>=3 and nonnegative one-trough real profiles (including plateaus). Independently checked 4,332 exact rational short profiles n=3..8, amplitudes 0..3; finite tests do not establish all-n theorem.

## originality

PASS

Best-of-knowledge statement-and-implication originality check after current primary reading and published-Resultary search. Equivalent forms, broader theorems, exact tables, and prior implication are assessed separately; residual risks are not hidden. The previously published monotone formula is a boundary case of this theorem; e.g. (1,0,...,0,1) is not monotone, has nontrivial deficit, and is not covered by either reflected monotone identity. Conjectured full-path inequality is not a theorem.

## value

PASS

Solves a natural genuinely nonmonotone, all-length single-trough class of the finite-path sharp-variation conjecture, beyond the prior full monotone subclass. The structural valley-preservation lemma and quantitative two-sided endpoint rigidity can be used in attempts to classify extremizers or reduce the remaining oscillatory cases; equality is sharp and nontrivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
