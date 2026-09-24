# Independent audit — root-number-1 non-cube-sum witnesses

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/046`  
**Audited source tree:** `ffc319bb778226eec58c9b0ef7d92e803c68f13e`  
**Review type:** separate AI independent audit.

## Claim audited

Among the ten least primes `l ≡ 7 (mod 9)` above 2000, all `n=3l` have global root number `+1`; for six listed primes, the cubic-residue test forces `h_3(12l)=1`, so the Das–Jha necessary condition proves that `3l` is not a sum of two rational cubes. The other four are explicitly left open.

## Correctness — PASS

I independently enumerated primes and confirmed the ten-prime window is `2113, 2131, 2203, 2221, 2239, 2293, 2311, 2347, 2383, 2437`, with next such prime 2473. Exact modular exponentiation gives `3^((l-1)/3) mod l = 438,1,1,1,295,1303,1428,1284,1,2351`, matching the record. Since these primes are `1 mod 3`, Euler's cubic-residue criterion applies.

The current full text of Das–Jha, arXiv:2508.05361v2, Lemma 2.4 states for `l ≡ 7 mod 9` that `h_3(12l)=2` iff `(3/l)_3=1`; Theorem A, via Lemma 2.4 and Proposition 2.6, gives the necessary condition that a cube-sum `3l` must have `h_3(12l)=2`. Thus the six nonunit residues yield `h_3=1` and the contrapositive proves non-cube-sum for `n=6339, 6717, 6879, 6933, 7041, 7311`. Das–Jha explicitly place the family `l ≡ 7 mod 9` in the root-number-1 case, so the record's hard-parity framing is correct. No conclusion is drawn for the four residue-one cases.

## Originality — PASS relative to checked literature

The general theorem and residue criterion are prior work, not new. I searched the Das–Jha full text and related cube-sum/Selmer literature for the ten primes and the six resulting witnesses; the checked paper does not list this consecutive `l>2000` window, and the exact residue outcomes are fresh finite computations rather than consequences that fix every prime in the congruence class. The originality claim is therefore limited to the explicit six-witness consecutive-window computation, not the theorem used to certify it.

## Scientific value — PASS

The surviving contribution is narrow but concrete: six rigorous examples in a natural root-number-1 family where parity itself is silent. Such explicit certified instances provide reproducible test cases for the class-group/Selmer obstruction and for computations on the corresponding Mordell curves. The record is appropriately labeled a partial census and does not inflate the four undecided cases into evidence.

No repair was needed. The main limitation is that all deep implications rely on the published Das–Jha theorem; this audit independently checked the finite arithmetic and theorem-to-record mapping rather than reproving their Selmer argument.

**Final disposition: PASSED.**
