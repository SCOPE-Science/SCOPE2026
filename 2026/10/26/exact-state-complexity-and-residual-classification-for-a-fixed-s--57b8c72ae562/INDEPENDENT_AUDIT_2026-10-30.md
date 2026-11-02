# Independent mathematical audit

## correctness

PASS

Concatenation N01(uv)=N01(u)+|u|_0|v|_1+N01(v) reduces residual to deficit t and zero count q. Cases are initial, accepting 0*, dead, one-future-one R_d=0^d1 0* (0≤d<k/2), and multiple-one Q_{q,t} with 1≤q≤floor(t/2), t≤k. Explicit 0 1^{k−t}0^{q−1} prefixes reach all pairs; 0^d1 and 1 0^{t−2q}1 distinguish all residuals. Count is floor(k²/4)+ceil(k/2)+3. Independently minimized reachable complete saturated-counter DFAs for each k=1..22; result matches with rejecting sink. Universal result relies on distinguishability proof.

## originality

PASS

Qualified PASS for exact minimal complete DFA size and full quotient types, not the generic fact of regularity or pattern counting. Mansour–Rastegar–Roitershtein 2019 §2.2 constructs automata preserving all continuation occurrence counts up to a bound; this is a finer equivalence than the exact-k Myhill–Nerode relation, so its displayed automata are not an explicit minimal quotient. Equivalent specializations through a general minimization framework remain a genuine risk.

## value

PASS

The exact-frequency scattered-subword family is a standard natural formal-language object. Complete residual classification, reachability and separating continuations explain the unexpected linear correction to quadratic state growth, rather than just giving a computed small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
