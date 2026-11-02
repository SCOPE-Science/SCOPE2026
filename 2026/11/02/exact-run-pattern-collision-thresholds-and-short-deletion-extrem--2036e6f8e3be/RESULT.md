# Exact run-pattern collision thresholds and short-deletion extremal counts

## Finding

The deletion-pattern bound is attained **exactly until a first, explicitly computable collision threshold**. For a word with maximal constant runs \(w=c_1^{\ell_1}c_2^{\ell_2}\cdots c_r^{\ell_r}\), where \(c_i\ne c_{i+1}\), define
\[
\delta(w)=1+\min_{\substack{i<j\\c_i=c_j}}\sum_{h=i+1}^{j-1}\ell_h,
\]
with \(\delta(w)=\infty\) when distinct runs never use the same letter. Let \(D_t(w)\) be the set of **distinct** words obtainable by deleting exactly \(t\) symbols. For every integer \(1\le t<|w|\),
\[
|D_t(w)|=[z^t]\prod_{i=1}^{r}(1+z+\cdots+z^{\ell_i})
\quad\Longleftrightarrow\quad t<\delta(w).
\tag{1}
\]
For every \(\delta(w)\le t<|w|\), the inequality is strict.

Consequently, for all integers \(n\ge r\ge1\), \(1\le t<n\), and alphabet sizes \(q\ge t+1\), write \(n=ar+s\) with \(a=\lfloor n/r\rfloor\), \(0\le s<r\). Then the **exact largest deletion-sphere size among all \(q\)-ary length-\(n\) words having exactly \(r\) runs** is
\[
\boxed{M_q(n,r,t)=[z^t](1+z+\cdots+z^a)^{r-s}
(1+z+\cdots+z^{a+1})^{s}.}
\tag{2}
\]
Every run-length arrangement with precisely \(s\) runs of length \(a+1\), the others of length \(a\), and successive run letters \(0,1,\ldots,q-1,0,1,\ldots\), attains this maximum. Thus (2) covers the previously unsettled regime \(r\nmid n\) for \(q\ge t+1\), including arbitrarily many runs \(r>q\).

The sufficient alphabet threshold is sharp as a uniform guarantee: at \(q=t\ge2\), \(n=r=t+1\), the right side of (2) equals \(t+1\), yet deleting \(t\) symbols leaves one letter, so the deletion sphere has size at most \(t\).

## Assumptions and scope

An alphabet of size \(q\) is a set of \(q\) distinct symbols; no algebraic structure is needed. A run is a maximal constant block of a finite word. A deletion pattern is an integer tuple \((d_1,\ldots,d_r)\) with \(0\le d_i\le\ell_i\) and \(\sum_i d_i=t\), interpreted as removing \(d_i\) letters from run \(i\). It determines one descendant but distinct patterns may determine the same descendant. The notation \([z^t]F(z)\) means the coefficient of \(z^t\) in a polynomial. All results are exact and finite; the optimized domain includes \(r=1\), \(r=n\), and \(r\nmid n\).

## Proof

**Step 1: deletion-pattern upper bound.** There are exactly \([z^t]\prod_i(1+z+\cdots+z^{\ell_i})\) admissible deletion tuples. The mapping from a tuple to its descendant is surjective, hence the sphere is at most that large.

**Step 2: injectivity before the threshold.** Suppose two different patterns, deleting fewer than \(\delta(w)\) letters, give the same word. Let \(i\) be the first run on which their retained counts differ, and name the patterns so that the first retains fewer symbols from run \(i\). The two generated outputs agree up to and including all symbols from runs preceding \(i\) and the shorter retained prefix from run \(i\). The next output symbol from the second pattern is \(c_i\), supplied by an additional retained letter of run \(i\). The first pattern has exhausted run \(i\), so to supply this symbol at the same output position it must advance to some later run \(j>i\) bearing \(c_j=c_i\), while deleting *every* symbol of intervening runs \(i+1,\ldots,j-1\). It also deletes at least one more symbol of run \(i\) than the second pattern. Its total deletion count is therefore at least \(1+\sum_{h=i+1}^{j-1}\ell_h\ge\delta(w)\), a contradiction. If no later matching run exists, equality of the outputs is impossible. Thus distinct patterns cannot collide for \(t<\delta(w)\).

**Step 3: collision at and beyond the threshold.** If \(\delta(w)<\infty\), choose runs \(i<j\) with equal symbols and minimum intervening length \(B=\sum_{h=i+1}^{j-1}\ell_h\). Delete all \(B\) intervening letters and one letter from run \(i\), or instead one from run \(j\). These are distinct patterns of \(B+1=\delta(w)\) deletions; both give exactly the same descendant because surviving portions of the equal-letter end runs concatenate, with the same combined length. For any \(t\) between \(B+1\) and \(|w|-1\), extend each pattern using the *same additional deletions per run*, with capacities \(\ell_i-1\) in run \(i\), \(\ell_j-1\) in run \(j\), zero in intervening runs, and full run length elsewhere. Total capacity is \(|w|-B-2\), at least \(t-B-1\). The patterns remain different, and their outputs remain identical. This establishes the strict inequality exactly when \(t\ge\delta(w)\), proving (1).

**Step 4: smoothing gives the universal upper bound.** Put \(Q_m(z)=1+z+\cdots+z^m\). If two run lengths satisfy \(a'\ge b'+2\), then
\[
Q_{a'-1}(z)Q_{b'+1}(z)-Q_{a'}(z)Q_{b'}(z)
=z^{b'+1}+z^{b'+2}+\cdots+z^{a'-1},
\]
a polynomial with nonnegative coefficients. Multiplying by the remaining run factors preserves coefficientwise nonnegativity. Repeatedly move one unit of length from any run at least two longer than another; the positive-integer lengths remain positive, and the sum of their squares strictly decreases, so the procedure terminates when all lengths differ by at most one. Its terminal multiset is exactly \(r-s\) copies of \(a\) and \(s\) copies of \(a+1\). Step 1 then bounds every deletion sphere by the right side of (2).

**Step 5: attaining the bound.** Assign successive runs symbols periodically from \(q\) distinct letters. Equal-symbol runs, when present, are separated by at least \(q-1\) complete nonempty runs; thus \(\delta(w)\ge q\). Since \(t<q\), Step 2 shows that distinct deletion patterns give distinct descendants. The run lengths are balanced by construction, so their polynomial coefficient is the right side of (2), which is attained. If there are fewer than \(q\) runs, all their symbols are distinct and injectivity is automatic.

**Step 6: sharpness of the alphabet condition.** Let \(q=t\ge2\) and \(n=r=t+1\). Every run has length one, so the formal pattern upper bound is \([z^t](1+z)^{t+1}=t+1\). Every descendant has length one and takes one of at most \(q=t\) values, so no word attains that upper bound. This proves sharpness as a universal sufficient alphabet threshold.

## Verification

A self-contained Python 3 standard-library script `verification/verify.py` implements an independent enumeration of deletion spheres via all position subsets, a separate run-pattern polynomial counter, and the proposed collision threshold. The stored `verification/verify_output.txt` reports 190840 tests of the threshold identity and its strict converse (for all deletion counts in prescribed short lengths), and 282205 exhaustive word checks covering 201 maximum-size parameter rows under \(q\ge t+1\). Seven sharp-threshold checks are included. All assertions passed. These are finite corroborations; the all-parameter claims rely on Steps 1–6, not on extrapolation.

As a numerical example, \((n,r,t,q)=(10,4,3,4)\) has \(a=2\), \(s=2\) and maximum \([z^3]Q_2(z)^2Q_3(z)^2=18\). The equal-length-upward comparison from a published corollary uses \([z^3]Q_3(z)^4=20\) in this short-deletion regime; the exact result therefore improves the bound in a concrete nondivisible case.

## Relationship to prior work

Li, Wang, and Fu (2026) establish nonbinary balanced-run extremality when the number of runs divides the word length, and provide an upper bound for the nondivisible case (their Corollary 15). Their conclusion explicitly leaves complete nondivisible extremality open. Equation (2) settles the short-deletion, sufficiently large-alphabet part of that parameter regime. Liron and Langberg (2012/2015), Section VII, define deletion patterns and prove the general pattern-count upper bound; those ingredients are known, and are not claimed as new. The novelty assessed here is the exact *if-and-only-if* collision threshold and the resulting sharp-alphabet exact extremal formula in the nondivisible regime. Mercier, Khabbazian, and Bhargava (2008) develop formulas for small deletion counts; the accessible abstract does not resolve whether it implicitly contains one of these conclusions. No priority claim is made concerning inaccessible text.

## Limitations

The extremal identity (2) is proved for \(q\ge t+1\), not for all smaller alphabets. The exact collision criterion (1), by contrast, holds without this alphabet restriction. The result determines a maximum cardinality and explicit attaining constructions, but it does not classify *all* maximizing words. The unavailable full text of the 2008 predecessor creates a residual priority uncertainty; a literature search is not proof of worldwide novelty. Independent mathematical review has not been performed.

## References

1. H. Li, X. Wang, F.-W. Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493, first public version 2026-01-10. https://arxiv.org/abs/2601.06493
2. Y. Liron, M. Langberg, *A Characterization of the Number of Subsequences Obtained via the Deletion Channel*, arXiv:1202.1644, first public version 2012-02-08. https://arxiv.org/abs/1202.1644
3. H. Mercier, M. Khabbazian, V. K. Bhargava, *On the Number of Subsequences When Deleting Symbols From a String*, IEEE Transactions on Information Theory 54 (2008), 3279–3285. https://doi.org/10.1109/TIT.2008.924730
