# Binomial transfer for the full run distribution of flattened parking functions

## Finding
For every integer \(n\geq 1\), a finite binomial-coefficient transfer recurrence computes
\[
F_{n,r}=\#\{a\in\operatorname{PF}_n:\ a\text{ is flattened and has exactly }r\text{ weakly increasing runs}\}
\]
for every \(1\leq r\leq\lceil n/2\rceil\). In particular it computes the complete run-count polynomial \(F_n(y)=\sum_r F_{n,r}y^r\) for unrestricted flattened parking functions, not only the insertion subclasses of the earlier literature. All transitions are nonnegative integers, and require neither enumeration of preference words nor any prior enumeration of parking functions.

Here is the exact recurrence. Fix \(n\), put \(K=\lceil n/2\rceil\), and let \(D_i(t,k,S)\) be indexed by \(0\leq i,t\leq n\), \(0\leq k\leq K\), and \(S\subseteq [k-1]\) (with \([0]=\varnothing\)). Initialize
\[
D_0(0,0,\varnothing)=1,
\]
with all other initial entries zero. For each \(i=1,\ldots,n\), from each state \(D_{i-1}(t,k,S)\) and each integer \(h\geq0\) with \(k+h\leq K\), choose any subset \(T\subseteq[k-1]\setminus S\). Put \(b=|S|\), \(q=|T|\), and \(a=t'-t\). Allow \(a\geq0\), \(t'\leq n\), and the parking-prefix constraint \(t'\geq i\). Make the update
\[
D_i(t',k+h,S\cup T)\mathrel{+}=D_{i-1}(t,k,S)\,W(a;k,b,h,q),
\]
where, using the ordinary convention that inadmissible binomial coefficients are zero,
\[
W(a;k,b,h,q)=
\begin{cases}
\binom{a-1}{h-1},&k=0,\ h\geq1,\ a\geq h,\\
\binom{a+b}{b+q+h},&k\geq1,\ a\geq q+h,\\
0,&\text{otherwise}.
\end{cases}
\]
After the \(n\) steps,
\[
\boxed{F_{n,r}=D_n(n,r,[r-1])\qquad(1\leq r\leq K).}
\]
The newly opened boundaries are deliberately *not* entered into \(S\) at their opening value; their strict descents can only be established using a greater letter.

The first run-count rows beyond the eight orders tabulated in the motivating paper are

| \(n\) | \((F_{n,1},F_{n,2},\ldots,F_{n,K})\) | total |
|:---:|:---|---:|
| 9 | (4862, 400257, 2201191, 1547655, 83946) | 4237911 |
| 10 | (16796, 2433340, 22084807, 28745746, 5031230) | 58311919 |
| 11 | (58786, 14780194, 212127438, 461537277, 174127144, 5915812) | 868546651 |
| 12 | (208012, 89935440, 1980589881, 6746765103, 4582660742, 493794095) | 13893953273 |

For illustration, the same recurrence yields \(\sum_r F_{20,r}=428524470238784969687\). The supplied checker computes the full ten-coefficient row at \(n=20\); that value and the numerical rows are consequences of the infinite recurrence, not separate claims of new published sequence priority.

## Assumptions and scope
A parking function of length \(n\) is a word \(a_1\cdots a_n\) with letters in \([n]\) such that its nondecreasing rearrangement \(a'_1\leq\cdots\leq a'_n\) obeys \(a'_j\leq j\) for every \(j\in[n]\). A *run* is a maximal contiguous weakly increasing subword. A parking function is *flattened* when the first letters of its runs are weakly increasing from left to right. Letters may repeat. Distinct words, not their cyclic rotations or multisets, are counted separately.

The recurrence applies for each fixed positive \(n\), with no asymptotic assumptions, and computes the distribution across every allowable number of runs. It does not assert a fixed-order scalar recurrence in \(n\) or a closed ordinary generating function.

## Proof
**1. Parking prefixes.** Let \(t_i\) be the number of letters of a word with value at most \(i\). The sorted parking inequalities are equivalent to \(t_i\geq i\) for all \(i\in[n]\). Thus processing letter values in increasing order and retaining only states with \(t_i\geq i\), with final total \(t_n=n\), enforces exactly the parking-function condition.

**2. Run-array representation.** A word with \(r\) weakly increasing runs has a unique array \((c_{i,j})\) of nonnegative integers, with \(c_{i,j}\) copies of value \(i\) in run \(j\). In each run these copies are necessarily in increasing value order. Conversely, such an array determines one concatenated word once each run is nonempty. Its run minima are weakly increasing precisely when the set of runs that have appeared by the end of each value level is an initial segment \(1,\ldots,k\). Runs started at the same letter value can be opened simultaneously in this order. This is the sole restriction on the starts of rows.

**3. Enforcing maximal runs.** Let \(m_{j+1}\) be the minimum in run \(j+1\). Its boundary is a genuine descent precisely when the maximum of run \(j\) is strictly greater than \(m_{j+1}\). This happens precisely when some value \(i>m_{j+1}\) is assigned to run \(j\). Upon completing all values at most \(i\), \(S\subseteq[k-1]\) records exactly those older boundaries where this has occurred. If run \(j+1\) starts at the current value, no assignment of that same value to run \(j\) can establish a strict descent. Hence at any step only already existing boundaries indexed below \(k\) can become newly satisfied. Every final array with all boundaries satisfied describes exactly the maximal weak-ascent runs of a flattened word. Every other array is excluded.

**4. Counting a transition.** At the next letter value, let \(h\) new runs begin. Let \(T\) be the \(q\) previously unsatisfied old boundaries newly fulfilled. A run indexed by \(j\in T\) must receive at least one copy of the current value; a run indexed by \(j\in[k-1]\setminus(S\cup T)\) must receive none. Each already satisfied boundary's preceding run, of which there are \(b=|S|\), can receive any nonnegative number. If \(k\geq1\), the old last run \(k\) can also receive any nonnegative number. The \(h\) newly opened runs each require at least one copy. Consequently the generating series for distributing new copies is
\[
x^{q+h}(1-x)^{-(b+q+h+1)}\quad(k\geq1),
\]
whose coefficient of \(x^a\) is \(\binom{a+b}{b+q+h}\). When \(k=0\), there are only the \(h\) new positive rows, giving series \((x/(1-x))^h\) and coefficient \(\binom{a-1}{h-1}\). These are exactly the displayed transition weights, including their zero conditions. All distributions represented by a transition are distinct and exhaustive.

**5. The endpoint.** A final state has placed all \(n\) letters, has exactly \(r\) opened runs, has weakly increasing run minima, has met every parking-prefix inequality, and has satisfied exactly all \(r-1\) required strict run boundaries. By the unique run-array representation it corresponds bijectively to an \(r\)-run flattened parking function. The endpoint formula follows.

**6. Run cutoff.** Each run preceding the last has length at least two: a singleton intermediate run, of value \(v\), could not simultaneously have a descent to the next run's starting letter \(w<v\) and satisfy the flattened requirement \(v\leq w\). Therefore \(n\geq2(r-1)+1\) and \(r\leq\lceil n/2\rceil\), proving that the state cutoff loses no object.

## Verification
The independent definitional checker enumerates every word in \([n]^n\) for \(1\leq n\leq6\), tests the sorted parking inequalities, constructs maximal weak-increase runs, and checks the order of their first letters. A second implementation distributes letters directly over started runs rather than using binomial weights. For \(1\leq n\leq12\) the latter agrees coefficientwise with the binomial recurrence. The full source table for \(1\leq n\leq8\) also agrees coefficientwise. Numerical rows \(n=9,10,11,12,15,20\) and the displayed \(n=20\) total are replayed. To check all of these with Python 3.10 or later, run `python3 verify.py`; expected final line is `VERIFY_OK`.

## Relationship to prior work
Elder, Harris, Markman, Tahir and Verga (2022 preprint; 2023 journal article) define flattened parking functions, tabulate their run distributions only up to length eight, and explicitly pose the enumeration of unrestricted flattened parking functions with a specified number of runs as an open problem. Their recursive methods enumerate much smaller insertion classes; the present recurrence treats unrestricted preference multiplicities with the parking-prefix condition.

Barrese, Elder, Harris and Simpson (2025) derive a fixed-reduced-content count for weakly flattened Fubini rankings, a related class of words. Their count is **unrefined by the number of runs**, and their Section 3.1 explicitly leaves the analogous run-distribution formula for Fubini rankings open. Their unrefined count can, with additional parking admissibility restrictions, be used to sum the overall number of flattened parking functions; it does not provide the specified-run recurrence above. Cruz and coauthors (2023) enumerate ordinary parking functions by descents and descent sets, without the extra order restriction on the starts of the runs. Baril, Harris and Ramírez (2024) study flattened Catalan words, which obey a local adjacent-letter condition rather than the sorted-multiset parking criterion.

## Limitations
This is a finite-state, \(n\)-dependent transfer algorithm, not a fixed-coefficient scalar recurrence or a closed-form generating function across all \(n\). Its number of states and transitions grows with \(n\). Exact proof establishes every \(n\geq1\); checks of finite examples are corroboration only. An independently authored mathematical audit has not been performed. Unindexed related results, including possible further refinements of the 2025 content formula, could affect priority.

## References
1. J. Elder, P. E. Harris, Z. Markman, I. Tahir and A. Verga, *On Flattened Parking Functions*, arXiv:2210.14206 (first public 2022-10-25); Journal of Integer Sequences 26 (2023), Article 23.5.8. https://arxiv.org/abs/2210.14206
2. K. Barrese, J. Elder, P. E. Harris and A. Simpson, *Enumerating Flat Fubini Rankings*, arXiv:2504.06466 (2025), especially Theorem 3.6 and Section 3.1. https://arxiv.org/abs/2504.06466
3. A. Cruz, P. E. Harris, K. J. Harry, J. Kretschmann, M. McClinton, A. Moon, J. O. Museus and E. Redmon, *On some discrete statistics of parking functions*, arXiv:2312.16786 (2023). https://arxiv.org/abs/2312.16786
4. J.-L. Baril, P. E. Harris and J. L. Ramírez, *Flattened Catalan Words*, arXiv:2405.05357 (2024). https://arxiv.org/abs/2405.05357
