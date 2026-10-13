# Exact Abelian factor spectra for a uniform one-marker substitution family

## Finding
For every integer \(b\ge 2\), define the length-\(b\) binary substitution
\[
\sigma_b(0)=0^{b-1}1,\qquad \sigma_b(1)=10^{b-1},
\]
and its one-sided fixed point \(\mathbf x_b=\sigma_b^\omega(0)\). For \(n\ge1\), let \(W_b(n)\) be the set of numbers of \(1\)'s among all factors of \(\mathbf x_b\) of length \(n\), and let \(a_b(n)=|W_b(n)|\) be the Abelian complexity. The following formulas determine **every** length's full Parikh spectrum, not just its cardinality.

If \(b=2\), then
\[
W_2(2q)=[q-1,q+1]\cap\mathbb Z\quad(q\ge1),\qquad
W_2(2q+1)=[q,q+1]\cap\mathbb Z\quad(q\ge0).
\]
For every \(b\ge3\), the spectra at lengths smaller than \(b\) are
\[
W_b(1)=\{0,1\},\qquad W_b(n)=\{0,1,2\}\quad(2\le n<b).
\]
At lengths \(n=bq+r\), where \(q\ge1\) and \(0\le r<b\), the spectra are
\[
W_b(bq+r)=
\begin{cases}
[q-1,q+2]\cap\mathbb Z,&2\le r\le b-2,\\
[q-1,q+1]\cap\mathbb Z,&r=0\text{ or }r=1,\\
[q,q+2]\cap\mathbb Z,&r=b-1.
\end{cases}
\]
(The first case is empty when \(b=3\).)

Consequently, for \(b\ge3\),
\[
a_b(n)=
\begin{cases}
2,&n=1,\\
4,&n>b\text{ and }2\le n\bmod b\le b-2,\\
3,&\text{otherwise}.
\end{cases}
\]
In particular the complexity is **purely periodic from length \(b\)**, with a valid period \(b\); it is constantly \(3\) at lengths \(n\ge2\) for \(b=3\). The exact maximal difference between weights of same-length factors is \(2\) for \(b=2,3\), and \(3\) for every \(b\ge4\).

## Assumptions and scope
Indices start at \(0\), and factors occur at arbitrary nonnegative starting positions. A spectrum interval \([u,v]\cap\mathbb Z\) means all integers from \(u\) to \(v\), inclusive. All substitutions are defined on the fixed binary alphabet \(\{0,1\}\); both substitution images contain precisely one \(1\), so this is a Parikh-constant family. The \(b=2\) member is the usual binary Thue–Morse substitution and is included only to display the sharp boundary of the family, not as a novelty claim.

No result here asserts eventual periodicity for **every** Parikh-constant substitution. The family is the natural one-marker interpolation between Thue–Morse at \(b=2\) and sparse binary blocks with the marker at opposite ends.

## Proof
Let \(x_j\in\{0,1\}\) denote the \(j\)th symbol of \(\mathbf x_b\). From the substitution itself,
\[
x_{bp}=x_p,\quad x_{bp+b-1}=1-x_p,\quad
x_{bp+s}=0\quad(1\le s\le b-2).
\tag{1}
\]
The interior condition is vacuous at \(b=2\). Both letter images have exactly one \(1\). Consequently, if \(F(N)=\sum_{j=0}^{N-1}x_j\), then for every \(p\ge0\) and \(0\le s<b\),
\[
F(bp+s)=p+\mathbf 1_{\{s>0\}}x_p.\tag{2}
\]

**Opposite pairs at every positive lag.** For all \(b\ge2\), \(\mathbf x_b\) is not ultimately periodic. When \(b=2\), this is the classical aperiodicity of Thue–Morse; it also follows directly from (1): \(x_{2p}=x_p\), \(x_{2p+1}=1-x_p\). If an eventual least period \(h=2k\) is even, the relation \(x_{2p}=x_p\) would give the smaller eventual period \(k\), a contradiction. If an eventual least period is odd, write \(h=2k+1\). The two parity classes of starting indices in \(x_{j+h}=x_j\) then give, for all sufficiently large \(p\),
\[
x_p=1-x_{p+k},\qquad 1-x_p=x_{p+k+1}.
\]
Applying the first identity at \(p+1\) and the second identity at \(p\) gives \(x_{p+1}=x_p\) eventually. That would make the word eventually constant, contradicting \(x_{2p+1}=1-x_p\). For \(b\ge3\), assume an eventual least period \(h\). If \(b\nmid h\), put \(d=\gcd(b,h)\). Then \(1\le d\le b-2\) and the positive multiples of \(h\) modulo \(b\) connect residue \(0\) to residue \(d\). But residue \(d\) is always \(0\) by (1), while residue \(0\) has infinitely many \(1\)'s by \(x_{bp}=x_p\) and the one-marker property, a contradiction. If \(b\mid h\), then \(x_{bp}=x_p\) turns eventual period \(h\) into smaller eventual period \(h/b\), again a contradiction.

Fix any lag \(h\ge1\). Neither \(x_{p+h}-x_p=1\) nor \(x_{p+h}-x_p=-1\) can be absent for all sufficiently large \(p\). Indeed, aperiodicity supplies infinitely many nonzero differences, while the telescoping identity
\[
\sum_{p=0}^{N-1}(x_{p+h}-x_p)
=\sum_{p=N}^{N+h-1}x_p-\sum_{p=0}^{h-1}x_p
\tag{3}
\]
remains bounded in absolute value by \(h\). Thus both ordered pairs \((0,1)\) and \((1,0)\) occur at separation \(h\), for every \(h\ge1\).

**Exact factor-weight reduction.** Write \(n=bq+r\), \(0\le r<b\). For a factor starting at \(bp+s\), where \(0\le s<b\), let \(t=\lfloor(s+r)/b\rfloor\) and \(u=s+r-bt\). Applying (2) at both ends yields the exact identity
\[
\#_1\bigl(x_{bp+s}\cdots x_{bp+s+n-1}\bigr)
=q+t+\mathbf 1_{\{u>0\}}x_{p+q+t}
-\mathbf 1_{\{s>0\}}x_p.\tag{4}
\]
This identity is valid for all \(p,q,r,s\) in the stated ranges, including \(q=0\). All endpoint extrema below are realized because (3) guarantees both oriented binary disagreements at every positive separation.

For \(b=2\), at even length \(r=0\), taking \(s=1\) in (4) gives \(q+x_{p+q}-x_p\). The two opposite disagreements realize both extremes \(q-1,q+1\), while \(s=0\) gives \(q\). At odd length \(r=1\), the two starting residues yield just \(q+x_{p+q}\) and \(q+1-x_p\), so the spectrum is \(\{q,q+1\}\).

Now let \(b\ge3\). We classify the weight extrema by the remainder \(r\):

* If \(r=0\) and \(q\ge1\), \(s=0\) gives weight \(q\), while \(1\le s<b\) gives \(q+x_{p+q}-x_p\). Thus the extremes are \(q-1\) and \(q+1\).
* If \(r=1\) and \(q\ge1\), \(s=0\) gives \(q+x_{p+q}\), any \(1\le s\le b-2\) gives \(q+x_{p+q}-x_p\), and \(s=b-1\) gives \(q+1-x_p\). The extremes are again \(q-1\) and \(q+1\). At \(q=0\), each expression is \(0\) or \(1\), and both occur.
* If \(2\le r\le b-2\) and \(q\ge1\), choosing \(1\le s<b-r\) yields \(q+x_{p+q}-x_p\), attaining minimum \(q-1\); choosing \(b-r<s<b\) yields \(q+1+x_{p+q+1}-x_p\), attaining maximum \(q+2\). All other start phases have values between these bounds. When \(q=0\), the first of these expressions is identically \(0\) and the second attains \(2\) at a \((0,1)\) pair of adjacent source symbols.
* If \(r=b-1\), the phases \(s=0\) and \(s=1\) give \(q+x_{p+q}\) and \(q+1-x_p\), respectively; phases \(s\ge2\) give \(q+1+x_{p+q+1}-x_p\). The exact extremes are \(q\) and \(q+2\), for all \(q\ge0\).

For every fixed \(n\), the number of \(1\)'s in length-\(n\) factors starting at successive positions changes by at most \(1\), since a window shift deletes one symbol and adds one symbol. Hence between attained minimum and maximum every intermediate integer is attained as well. This proves all displayed exact spectra and the Abelian-complexity formula.

Finally, the maximum difference of equal-length factor weights is the largest spectrum width. The tables give width \(2\) for \(b=2\) and \(b=3\). For any \(b\ge4\), taking \(n=b+2\) produces the interval \([0,3]\cap\mathbb Z\), attaining width \(3\). This proves the sharp balance constants.

## Verification
Run `python3 verify.py` in the same folder as `certificate.json`. The independent verifier compares a substitution-generated prefix with the index recurrence in (1), checks the prefix-count formula (2), and compares exhaustive observed factor weights with the theorem's exact integer intervals for multiple parameters and lengths.

It also checks the two mismatch orientations at each tested lag and separately checks all symbolic boundary states \((s,r,q)\) against the bounds in the theorem. This is finite regression testing only. The proof above obtains the infinite conclusion for every \(b\ge2\) and \(n\ge1\) from (1)–(4) and aperiodicity.

## Relationship to prior work
Rigo, Stipulanti, and Whiteland prove that fixed points of Parikh-collinear morphisms have automatic Abelian complexity and give a general effective method. Their 2024 paper explicitly asks whether **every** Parikh-constant morphism has ultimately periodic Abelian complexity. Their examples use other morphisms and do not give the present all-parameter factor-weight spectra. This paper resolves the periodicity question **only for the specified one-marker family** and determines every attainable Parikh vector and the exact balance constant.

Their 2023 predecessor treats automaticity and supplies a different binary Parikh-collinear example with a non-ultimately-periodic Abelian-complexity function; this does not cover the present Parikh-constant family. The classical Thue–Morse Abelian-complexity values for \(b=2\) are known and used here as a boundary comparison, not claimed as new.

## Limitations
The statement concerns the special two-letter length-\(b\) substitutions with one marker at opposite ends. It does not settle the open periodicity question for all Parikh-constant morphisms, nor does it determine ordinary factor complexity or higher binomial complexity. The targeted literature search did not locate a previously published formula for this family, but an unindexed equivalent derivation remains a residual originality risk.

## References
1. M. Rigo, M. Stipulanti, and M. A. Whiteland, “Automatic Abelian Complexities of Parikh-Collinear Fixed Points,” arXiv:2405.18032v1 (first public 2024-05-28), *Theory of Computing Systems* (2024), DOI 10.1007/s00224-024-10197-5.
2. M. Rigo, M. Stipulanti, and M. A. Whiteland, “Automaticity and Parikh-collinear Morphisms,” *Combinatorics on Words* (WORDS 2023), Lecture Notes in Computer Science 13899, pp. 247–260, DOI 10.1007/978-3-031-33180-0_19.
3. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), DOI 10.1017/CBO9780511546563.
4. J. Shallit, “Abelian Complexity and Synchronization,” *Integers* 21 (2021), Article A36.
