# Independent mathematical audit

## correctness

PASS

With margins x=i and y=n-1-j, let p=n-1-x-y. For a valid shift, the two ones either occupy singleton chains (giving the suffix of periods beginning at n-min(x,y)) or occupy one complete two-element chain (shift p, with x,y<p). At fixed exceptional p, the ordered margins sum to n-p-1 and range over R=min(n-p,3p-n) choices for the left margin, positive exactly for p>floor(n/3). The threshold determines the unordered margin pair, so there are ceil(R/2) profiles, and the unique possible singleton for this p lies at equal margins and occurs exactly when R is odd. For p<=n-2 the gap from p to the suffix threshold is max(x,y)+1>=2; only p=n-1 duplicates a pure suffix. Adjacent markers realize all floor(n/2) suffixes for n>=4. Their reversals are distinct except for the minimum threshold at even n, where no other pure word has those margins; at n=4 the endpoint pair duplicates this exceptional singleton. Since R has the parity of p-n, this proves the asserted U(n). Splitting the sum at floor(n/2) gives 12 times the six correction constants as 12,21,8,21,12,17; n=2,3 are separate direct cases. A fresh bounded test compared every potential shift against all overlap pairs incident to a one, for 147440 words over all 2<=n<=96, and reproduced the structural formula, profile counts and singleton counts. Replay: node /workspace/checks/geometry-and-word-reproduction.js. The bounded check corroborates rather than replaces the chain and margin arguments. Neither cyclic shifts nor uniqueness modulo reversal was tested or claimed.

## originality

PASS

The inspected antecedents cover unrestricted autocorrelation sets or a different observation on sparse words. They do not establish the fixed-source-weight-two counts or the labeled singleton classification. This is a bounded best-of-knowledge finding; it does not claim originality of the definition of period or priority for arbitrary period-set enumeration.

## value

PASS

The result gives the complete sparsest nontrivial two-position profile classification and a sharp distinction between identifying a word and merely realizing an autocorrelation pattern. It identifies when a gap is visible, quantifies the resulting collisions with an exact residue correction, and detects the labeled uniqueness exceptions that an unrestricted admissibility count does not see. These are substantive exact invariants of the observation model, rather than a small-instance recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
