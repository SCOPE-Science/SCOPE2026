# Independent mathematical audit

## correctness

PASS

Reconstructed both languages and all reachable continuation classes in RESULT.md lines 33–65. For a nonpower, 2^k−c for k≥s has binary expansion α at k=s and 1^(k−s)β for k>s; prefixing zeros gives 0*( {α} ∪ 1+β ). It is essential that β starts with zero and |α|<s. Beyond a nonzero prefix, before its first zero the r exceptional suffixes augment 1*β by distinct words shorter than s; a longer initial run reaches 1*β alone. After consuming the first zero, exactly h overlap-prefix lengths leave two suffixes; the longer suffix distinguishes the h pairs. Singletons are precisely the s proper suffixes of β, including the empty suffix, since exceptional-only suffixes also occur among them. The start residual alone has accepted words with arbitrarily many initial zeros, and an impossible prefix reaches the empty residual. For c=2^(s−1), the language 0*({ε} ∪ 1+0^(s−1)) gives the start, sink, 1*0^(s−1), and s−1 singletons, including the s=1 case with no singletons. The bounds follow from 1≤r+h≤|α|≤s−1 and the two stated choices of c realize the endpoints, including their coincidence at s=2. Inspected the bundled checker and saved finite output; the source script was not executed, and the proof is independent of the finite test range.

## originality

PASS

The prior logarithmic upper bound and related construction for the identical shifted indicator are credited. The inspected evidence does not already give the minimal complete count, its dependence on bits of c, or the sharp dyadic envelope. This is a bounded statement comparison, not a priority guarantee.

## value

PASS

This is the full exact classification of a natural translated automatic indicator already used as a state-complexity example. The formula separates shifts in the same size band that differ by up to s−2 states and identifies the combinatorial information needed to predict those states. A qualitative upper bound, or minimizing each chosen shift separately, cannot answer that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
