# Sharp size-two string-attractor phase diagram for four-run binary words

## Finding

For all positive integers \(a,b,c,d\), consider the binary word
\[
W=0^a1^b0^c1^d.
\]
Let \(\gamma^*(W)\) be its smallest string-attractor cardinality. Then \(\gamma^*(W)\) is always \(2\) or \(3\), and the complete phase diagram is
\[
\boxed{\gamma^*(W)=3\iff
(a>c\ \text{and}\ d>b)\quad\text{or}\quad(c\ge a+2\ \text{and}\ b\ge d+2).}
\]
Every other parameter quadruple has \(\gamma^*(W)=2\). In that regime **all** smallest attractors are classified by the four families below; no other pair qualifies. Their exact count is \(N_2=\alpha+\beta+\chi+\delta-\varepsilon\), with the explicit parameters specified below. In the \(\gamma^*=3\) regime, this formula gives \(N_2=0\); enumeration of all three-position minimizers is not claimed.

Number positions from \(1\). Write the four disjoint consecutive position intervals as
\[
A=[1,a],\quad B=[a+1,a+b],\quad C=[a+b+1,a+b+c],\quad D=[a+b+c+1,a+b+c+d].
\]
Let \(B_\mathrm{last}=a+b\) and \(C_\mathrm{first}=a+b+1\). The four families of attractor pairs are:

1. **Family I:** if \(a\ge c\) and \(b\ge d\), choose \(\{B_\mathrm{last},x\}\), where \(x\) is **any** position of \(A\) when \(b=1\), and is otherwise only the last position of \(A\).
2. **Family II:** if \(c\ge a\) and \(b\ge d\), choose \(\{B_\mathrm{last},x\}\) with \(x\in C\): when \(b=1\), take any of the last \(\min(c,a+1)\) positions of \(C\); when \(b\ge2\), the only possible choice is the last position of \(C\), and it exists precisely when \(b\le d+1\).
3. **Family III:** if \(c\ge a\) and \(d\ge b\), choose \(\{C_\mathrm{first},y\}\), where \(y\) is **any** position of \(D\) when \(c=1\), and is otherwise only the first position of \(D\).
4. **Family IV:** if \(c\ge a\) and \(b\ge d\), choose \(\{C_\mathrm{first},y\}\) with \(y\in B\): when \(c=1\), take any of the first \(\min(b,d+1)\) positions of \(B\); when \(c\ge2\), the only possible choice is the first position of \(B\), and it exists precisely when \(c\le a+1\).

The only possible duplicate between families is the pair \(\{B_\mathrm{last},C_\mathrm{first}\}\), appearing in II and IV simultaneously. For a fully numerical count, set
\[
\begin{aligned}
\alpha&=\mathbf1_{a\ge c,\ b\ge d}\begin{cases}a,&b=1,\\1,&b>1;\end{cases}\\
\beta&=\mathbf1_{c\ge a,\ b\ge d}\begin{cases}\min(c,a+1),&b=1,\\\mathbf1_{b\le d+1},&b>1;\end{cases}\\
\chi&=\mathbf1_{c\ge a,\ d\ge b}\begin{cases}d,&c=1,\\1,&c>1;\end{cases}\\
\delta&=\mathbf1_{c\ge a,\ b\ge d}\begin{cases}\min(b,d+1),&c=1,\\\mathbf1_{c\le a+1},&c>1.\end{cases}
\end{aligned}
\]
Here an indicator is \(1\) when all subscript conditions hold and \(0\) otherwise. Define
\[
\varepsilon=\mathbf1_{\bigl(b=d=1\ \text{and}\ a\le c\le a+1\bigr)\ \text{or}\ \bigl(a=c=1\ \text{and}\ d\le b\le d+1\bigr)}.
\]
Then the exact number of two-position attractors is
\[
\boxed{N_2(a,b,c,d)=\alpha+\beta+\chi+\delta-\varepsilon.}
\]
For example, \(N_2(2,2,2,2)=4\), whereas \(N_2(2,1,1,2)=N_2(1,3,3,1)=0\). The alternating word \(0101\) has \(N_2(1,1,1,1)=3\).

## Assumptions and scope

A **factor** is a nonempty contiguous substring. A **string attractor** \(\Gamma\subseteq\{1,\dots,|W|\}\) means that every distinct factor of \(W\) has at least one occurrence whose closed position interval intersects \(\Gamma\). The four run lengths are positive integers without an upper bound. Both symbols must occur, so the trivial alphabet lower bound is \(\gamma^*(W)\ge2\). The result concerns linear, not circular, factors; positions are labeled and one-indexed. The primary subject is combinatorics on words (MSC2020 \(68R15\)).

## Proof

**Step 1: A factor trichotomy.** Every nonempty factor of \(W\) is (i) a constant run \(0^i\) or \(1^j\); (ii) a factor containing the central unique transition \(10\) from the second run to the third; or (iii) a mixed factor \(0^i1^j\) with positive exponents occurring across either the first \(01\) boundary (with \(i\le a,j\le b\)) or the last \(01\) boundary (with \(i\le c,j\le d\)). This is exhaustive because the only transitions are \(01,10,01\), and a factor crossing at least two of them contains the central transition. The factor \(10\) occurs only at the central boundary. Therefore, any attractor must contain the last position of \(B\) or the first position of \(C\). Furthermore, a two-position attractor must contain exactly one zero-position and one one-position, since factors \(0\) and \(1\) both have to be attracted.

**Step 2: Three positions suffice.** If \(a\ge c\), choose the last positions of \(A,B\), and the first position of \(D\). If \(a<c\), choose the first positions of \(B,C,D\). In either case, a selected position lies inside a longest zero-run and a longest one-run. Both \(01\) boundaries are covered by a selected endpoint; the central \(10\) boundary is covered by a selected endpoint. By Step 1, all factors are attracted. Thus \(\gamma^*(W)\le3\).

**Step 3: Pairs using the last position of \(B\).** Put \(p=B_\mathrm{last}\) into a candidate pair. Its other position is necessarily a zero in \(A\) or \(C\). If it is in \(A\), the constant factors \(0^{\max(a,c)}\) and \(1^{\max(b,d)}\) force \(a\ge c\) and \(b\ge d\). If \(b>1\), the factor \(01\) forces the chosen position to be the last zero of \(A\), because \(p\) is not the first one of \(B\). If \(b=1\), every position of \(A\) works: every \(01\)-type factor occurring across the last boundary also occurs across the first and crosses \(p\). Conversely, the specified pairs cover all constant factors, all factors crossing the central boundary, and all \(01\)-type factors. This is exactly Family I.

If the other position is in \(C\), the constant factors force \(c\ge a\) and \(b\ge d\). For \(b>1\), the factor \(01\) forces the last zero of \(C\). Every \(0^i1^j\) with \(j=b\) that occurs at the first boundary crosses \(p\). For \(1\le j<b\), the first-boundary occurrence misses \(p\), so all such patterns must also occur at the last boundary, where the chosen final zero of \(C\) catches them. Equivalently \(d\ge b-1\) (the zero inequality already gives \(c\ge a\)). Necessity follows already by taking \(0^11^{b-1}\); sufficiency follows from the factor trichotomy. For \(b=1\), all first-boundary \(01\)-type factors cross \(p\), while the remaining last-boundary-only factors are exactly \(0^i1\) with \(a<i\le c\). A position of \(C\) catches all of these if and only if it is among the last \(\min(c,a+1)\) zeros of \(C\). This proves Family II, including both the necessity and sufficiency of its boundary cases.

**Step 4: Pairs using the first position of \(C\).** Reverse the word and complement each binary symbol. This symmetry preserves all factor occurrences, selected-position intersections and attractor cardinalities, and maps the run-length tuple \((a,b,c,d)\) to \((d,c,b,a)\). It interchanges the roles of the last position of the second run and the first position of the third run. Applying Step 3 to the transformed tuple and translating positions back gives exactly Families III and IV. Every pair contains one of those central positions by Step 1, so the four families are exhaustive. Their sufficiency is already established by Step 3 and symmetry.

**Step 5: Phase diagram and count.** Family I exists exactly when \(a\ge c,b\ge d\), and Family III exactly when \(c\ge a,d\ge b\). Families II and IV add precisely the crossing regime \(c\ge a,b\ge d\) whenever, respectively, \(b-d\le1\) or \(c-a\le1\). Hence **no** family exists exactly when (a) \(a>c,d>b\), or (b) \(c-a\ge2,b-d\ge2\); these are disjoint regions. Step 2 then makes the minimum \(3\) in those regions and \(2\) otherwise. The four family sizes are \(\alpha,\beta,\chi,\delta\). Distinct families cannot have the same pair except II and IV; their intersection is the single central pair, which appears exactly under the displayed \(\varepsilon\) condition. Inclusion-exclusion completes the exact enumeration.

## Verification

The accompanying independent standard-library Python program, `verify.py`, enumerates all candidate pairs directly from literal factors, without assuming the classification, for all \(1\le a,b,c,d\le6\) (\(1296\) quadruples and \(125496\) pair tests). It compares each exact pair set against the four analytic families and confirms the two sharp failure regions. For all \(1\le a,b,c,d\le3\), it additionally checks \(2376\) pairs using a separately written literal occurrence test rather than factor bit masks. In all \(325\) phase-three quadruples within the larger test range, an explicitly constructed three-position set is independently verified to cover every factor. This finite experiment corroborates the theorem but is **not** the proof for unbounded parameters; that proof is Steps 1–5.

Reproduce with `python3 verify.py` from the files extracted from this finding. No external packages or datasets are required. The expected output begins `VERIFY_OK quadruples=1296`.

## Relationship to prior work

String attractors and the alphabet lower bound are classical (Kempa and Prezza, 2017/2018). Mantaci, Restivo, Romana, Rosone and Sciortino investigate attractors in several families of finite words, include nontrivial binary two-attractor examples, and explicitly pose the larger problem of identifying binary words admitting two-position attractors. Restivo, Romana and Sciortino later develop attractor-based complexity functions for infinite words. The present result is a complete **four-run, arbitrary-run-length** solution of the size-two boundary, including an exact enumeration of every two-position minimizer and the two sharp three-position obstruction regions. Neither general upper bounds nor examples of other word families imply the phase diagram.

A previously recorded special case describes all minimum attractors of two-run powers \((0^a1^b)^k\); its \(k=2\) instance is covered by the equality subfamily \(a=c,b=d\) here. That known instance and the alternating word are **not** claimed to be newly discovered. The added contribution is the unrestricted four-parameter classification, especially the regimes requiring three positions. The precise comparisons and residual uncertainty about unindexed equivalent results appear in the accompanying review.

## Limitations

The theorem is restricted to words having exactly four alternating nonempty binary runs, or their reverse/complement images. It does not classify **all** minimum three-position attractors in the phase-three regime, though it proves that three suffice and two cannot. It does not address arbitrary binary words, longer run sequences, circular attractors, or algorithmic complexity of the general attractor problem. Mathematical correctness is supported by a complete proof and finite consistency tests; originality is qualified by possible unlocated equivalent treatments. Independent external auditing has not been performed.

## References

1. D. Kempa and N. Prezza, *At the Roots of Dictionary Compression: String Attractors*, arXiv:1710.10964 (first public 2017-10-30), especially the definition and compression context.
2. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (first public 2019-07-10), especially sections on finite binary families.
3. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science **850** (2021), 236–248, DOI:10.1016/j.tcs.2020.11.006, especially Example 24 and the two-attractor classification question.
4. A. Restivo, G. Romana, M. Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376 (first public 2022-06-01), for comparison with attractor-based infinite-word complexity.
