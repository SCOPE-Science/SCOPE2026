# Independent audit — 2026-09-22

Record: SCOPE-20260909-021. Examined 2026-09-26.

## Correctness — PASS
I independently recounted the cliques of every one of the 995 committed connected graph representatives (n=2,…,7) and expanded the rational denominator `Q(t)=Σ c_k(-t)^k(1+t)^(w-k)`; all 995 clique vectors and denominators match the table. There are eleven seven-vertex trees, each with `Q=1−5t`. For all 971 non-trees, an independent exact certificate is especially simple: if d=deg Q, every coefficient of `5^d(1+x)^d Q(x/[5(1+x)])` is nonnegative, with positive constant and leading coefficients. Hence Q has no zero in `0≤t≤1/5`; the eleven trees alone attain rate five. The next denominator `1−4t−4t²` has rate `2+2√2` (18 table rows), giving gap `3−2√2`. The committed verifier also completed `VERIFY_OK`, including exact Sturm checks and Tits-representation radius-five sphere counts on all 995 graphs. The verifier's opening docstring mistakenly says `2+√2`; its operative code, table and RESULT give `2+2√2`.

## Originality — PASS, bounded
The spherical-growth identity itself is classical, explicitly recorded by Okun and Scott; all tree denominators `1−(n−2)t` follow immediately. The new finite result is the exhaustive n≤7 comparison, exact runner-up and graph-indexed 995-row denominator table. I found no matching finite table in the checked Coxeter-growth literature; this is a limited search claim, not a claim to invent the rational formula.

## Scientific value — PASS, bounded
The exact small-graph classification and runner-up provide a reproducible benchmark for growth comparisons. Its scope is finite and the maximal tree rate alone is elementary. Enumeration completeness uses the known connected-unlabelled graph counts plus the candidate graph generator; I independently checked every listed graph and all 995 denominator entries, not a separate reconstruction of the unlabeled census.

Sources: [Okun–Scott, arXiv:1812.07755](https://arxiv.org/abs/1812.07755); [Ciobanu–Kolpakov, arXiv:1504.02774](https://arxiv.org/abs/1504.02774); [OEIS A001349](https://oeis.org/A001349). Repository evidence: `artifacts/graphs.json`, `table.json`, `verify.py`, `RESULT.md`.
