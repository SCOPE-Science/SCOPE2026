# Exact minimum string attractors for two Rudin–Shapiro dyadic prefixes

## Finding

Let \(R=(R_j)_{j\geq0}\) be the binary Rudin–Shapiro sequence, in which \(R_j\) is the parity of the number of overlapping occurrences of \(11\) in the usual binary expansion of \(j\). Write \(R_n=R[0..n-1]\), and let \(\gamma(w)\) denote the smallest cardinality of a string attractor of a finite word \(w\). Then

\[
\boxed{\gamma(R_{128})=10,\qquad \gamma(R_{256})=11.}
\]

In zero-based indexing, respective optimal attractors are

\[
\begin{aligned}
P_{128}&=\{32,47,56,69,75,82,91,100,107,118\},\\
P_{256}&=\{63,88,104,112,139,154,164,184,195,208,238\}.
\end{aligned}
\]

## Assumptions and scope

The alphabet is \(\{0,1\}\), positions run from \(0\) to \(n-1\), and the word is a *finite prefix* of the standard Rudin–Shapiro word (not a cyclic word). A string attractor \(P\) is a subset of positions such that for every nonempty distinct factor \(u\) there is some occurrence \(w[i..i+|u|-1]=u\) whose interval intersects \(P\). The claim concerns exactly \(n=128\) and \(n=256\); it is not an asymptotic statement.

## Proof

For a nonempty factor \(u\), define the binary position mask

\[
M_u=\bigcup_{\substack{0\leq i\leq n-|u|\\w[i..i+|u|-1]=u}}
\{i,i+1,\ldots,i+|u|-1\}.
\]

Here \(M_u\) is represented computationally as an integer whose set bits are precisely its positions. Directly from the definition, \(P\) is an attractor exactly when \(P\cap M_u\ne\varnothing\) for every nonempty distinct factor. There are respectively \(7008\) and \(28128\) such factors; the attached verifier enumerates *all* lengths and all starts, without truncation or sampling. It checks that the two displayed position sets meet every factor mask, proving \(\gamma(R_{128})\leq10\) and \(\gamma(R_{256})\leq11\).

For the lower bounds, consider the finite family of masks \(M_u\). If \(M_v\subseteq M_u\), then any set meeting \(M_v\) automatically meets \(M_u\). Consequently the family may be reduced, without changing its hitting sets, by retaining inclusion-minimal masks. Exhaustive reduction produces respectively \(48\) and \(64\) masks; the verifier checks that *every* original mask contains a retained mask.

The remaining problem is an exact finite hitting-set decision problem. Represent the uncovered retained masks by a bitset \(U\) and, for each possible selected position \(p\), denote by \(B_p\) the bitset of masks containing \(p\). Every hitting set of size at most \(k\) must select a position from each uncovered mask, so one may choose an uncovered mask, branch on all its positions, and recurse to \(U\setminus B_p\) with budget \(k-1\). Two pruning operations preserve completeness: identical coverage bitsets have identical effect, and a choice whose covered-mask set is contained in another choice's covered-mask set is dominated. A memoized failure for a particular uncovered-mask set and budget also proves failure at the same uncovered-mask set with no greater budget. This is an exhaustive search, not a numerical optimization assertion. The supplied executable runs it to completion at budgets \(k=9\) and \(k=10\), respectively. It obtains no feasible hitting set, visiting respectively \(243\) and \(3703\) recursive nodes. Hence \(\gamma(R_{128})\geq10\) and \(\gamma(R_{256})\geq11\). Combined with the witnesses, both equalities follow.

## Verification

Run `python3 artifacts/verify_attractors.py` from the extracted scientific package. It uses only the Python standard library, regenerates both words, enumerates every factor occurrence, confirms both witnesses against the complete unreduced factor families, proves that the reduced mask families are equivalent, and explores the exact lower-bound search trees. Expected final output: `RUDIN_SHAPIRO_ATTRACTORS_VERIFY_OK`. It reports the four exact counts (factor count, retained masks, optimal size, and lower-bound search nodes) for each length. The proof is finite and exhaustive at the two specified lengths.

## Relationship to prior work

Béal, Crochemore and Romana, *Checking and producing word attractors*, arXiv:2509.08503 (first public September 10, 2025), develop checking and greedy construction algorithms and report experiments for several named word families; their experimental section does not list Rudin–Shapiro or these two optimum values. Schaeffer and Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, establish general theory for automatic words but do not supply the two exact values. The published mathematical record `2026/9/8/SCOPE079` determines Rudin–Shapiro dyadic optima through length \(64\) and reports verified upper bounds \(12\) and \(13\) at lengths \(128\) and \(256\), respectively; those upper bounds do not determine the new exact values. No claim of novelty is made for the definition, reduction to hitting set, or general exhaustive-search methodology.

## Limitations

These are two exact finite-prefix measurements, not a formula for all dyadic prefix lengths or a classification of every smallest attractor. The verifier proves the stated two cases by finite exhaustion and is not an infinite theorem. Independent verification and definitive literature-priority determination have not been performed.

## References

1. Marie-Pierre Béal, Maxime Crochemore, Giuseppe Romana, *Checking and producing word attractors*, arXiv:2509.08503v1 (2025), https://arxiv.org/abs/2509.08503.
2. Luke Schaeffer, Jeffrey Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (2020), https://arxiv.org/abs/2012.06840.
3. *Exact minimal string attractors for Rudin-Shapiro and regular-paperfolding dyadic prefixes (n<=64) with certified bounds to n=1024*, public record `2026/9/8/SCOPE079`, https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE079.
