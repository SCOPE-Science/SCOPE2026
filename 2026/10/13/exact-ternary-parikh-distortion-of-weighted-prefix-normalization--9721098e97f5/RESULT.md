# Exact ternary Parikh distortion of weighted prefix normalization
## Finding
Let \(\Sigma=\{\mathtt a<\mathtt b<\mathtt c\}\) have the standard weight measure
\[
\mu(\mathtt a)=1,\qquad \mu(\mathtt b)=2,\qquad \mu(\mathtt c)=3.
\]
For a word \(w\), write \(F_w(k)\) for the maximum \(\mu\)-weight of a factor of \(w\) of length \(k\). Two words are factor-weight equivalent when all their values \(F_w(k)\) agree. Let \(\operatorname{PNF}(w)\) denote the unique weighted prefix normal form under this standard measure.

For every integer \(n\ge2\), if
\[
D_n=\max_{w\in\Sigma^n}
\left\|\operatorname{Parikh}(w)-\operatorname{Parikh}(\operatorname{PNF}(w))\right\|_1,
\]
then
\[
D_n=4\left\lfloor\frac{n-2}{2}\right\rfloor.
\]

In fact a stronger statement holds. If \(u,v\in\Sigma^n\) are factor-weight equivalent, then for some integer \(t\),
\[
\operatorname{Parikh}(v)-\operatorname{Parikh}(u)=(t,-2t,t)
\]
and
\[
|t|\le\left\lfloor\frac{n-2}{2}\right\rfloor.
\]
The bound is sharp for every \(n\ge2\), already for pairs in which one member is the weighted prefix normal form of the other.

## Assumptions and scope
The Parikh vector is ordered as
\[
(|w|_{\mathtt a},|w|_{\mathtt b},|w|_{\mathtt c}).
\]
The distance in the finding is ordinary \(\ell_1\)-distance on these three integer coordinates.

The result concerns the ternary standard weight measure from the weighted-prefix-normal framework. It makes no assertion for non-arithmetic or gapful weight measures, nor for alphabets with four or more letters.

## Proof
Factor-weight equivalent words have the same length and the same total weight, because the final factor-weight value is the weight of the whole word. Suppose
\[
\operatorname{Parikh}(v)-\operatorname{Parikh}(u)=(x,y,z).
\]
Equal length and equal total weight give
\[
x+y+z=0,\qquad x+2y+3z=0.
\]
Subtracting twice the first equality from the second gives \(z=x\), and then \(y=-2x\). Hence the difference is \((t,-2t,t)\).

Swap \(u\) and \(v\) if needed, so \(t>0\). Since \(v\) has more \(\mathtt c\)'s, it contains a \(\mathtt c\). Therefore
\[
F_v(1)=3.
\]
Factor-weight equivalence forces \(F_u(1)=3\), so \(u\) also contains at least one \(\mathtt c\). Moreover \(u\) contains at least \(2t\) copies of \(\mathtt b\), because \(v\) contains \(2t\) fewer. Consequently
\[
n\ge2t+1.
\]
For even \(n\), this already gives
\[
t\le\left\lfloor\frac{n-2}{2}\right\rfloor.
\]

Now let \(n=2r+1\) be odd. The preceding inequality gives \(t\le r\). If equality held, all count inequalities would be tight: \(u\) would have Parikh vector
\[
(0,2r,1)
\]
and \(v\) would have Parikh vector
\[
(r,0,r+1).
\]
Every word with the first vector has a length-two factor \(\mathtt{bc}\) or \(\mathtt{cb}\), hence \(F_u(2)=5\). A word with the second vector uses only \(\mathtt a\) and \(\mathtt c\). Its length-two factors have weights \(2\), \(4\), or \(6\), so its maximum is never \(5\). This contradicts factor-weight equivalence. Therefore \(t\le r-1=\lfloor(n-2)/2\rfloor\).

It remains to attain the bound. For even \(n=2r\), set
\[
w=\mathtt{bc}(\mathtt{ac})^{r-1},
\qquad
p=\mathtt c\mathtt b^{\,2r-1}.
\]
Relative to the baseline weight \(2\), the letter-weight deviations in \(w\) are
\[
0,1,-1,1,-1,\ldots,-1,1.
\]
Every factor has deviation at most \(1\), and for every factor length there is a factor with deviation exactly \(1\). Thus
\[
F_w(k)=2k+1
\]
for every \(1\le k\le n\). The prefixes of \(p\) have exactly these weights, so \(p=\operatorname{PNF}(w)\). Their Parikh vectors differ by
\[
(r-1,-2r+2,r-1),
\]
whose \(\ell_1\)-norm is \(4(r-1)\).

For odd \(n=2r+1\), set
\[
w=\mathtt{abc}(\mathtt{ac})^{r-1},
\qquad
p=\mathtt c\mathtt b^{\,2r-1}\mathtt a.
\]
The deviation sequence of \(w\) is
\[
-1,0,1,-1,1,\ldots,-1,1.
\]
For every proper factor length \(k<n\), the maximum deviation is \(1\), while the total deviation is \(0\). Hence
\[
F_w(k)=2k+1\quad(1\le k<n),\qquad F_w(n)=2n.
\]
These are exactly the prefix weights of \(p\), so again \(p=\operatorname{PNF}(w)\). The Parikh-vector difference has parameter \(t=r-1\), giving \(\ell_1\)-distance \(4(r-1)\). This proves sharpness.

## Verification
The bundled `verify.py` independently reconstructs factor-weight signatures. It exhaustively checks every ternary word of lengths \(2\) through \(9\), totaling \(29{,}520\) words. For each signature it reconstructs the weighted prefix normal form from successive signature differences, checks that the reconstructed form has the same signature, computes the largest Parikh displacement to the form, and computes the largest \(\mathtt c\)-count spread inside an equivalence class.

The exhaustive maxima agree with the theorem:
\[
0,0,4,4,8,8,12,12
\]
for the \(\ell_1\)-distortion at lengths \(2,\ldots,9\). The checker also verifies the two infinite witness families algebraically at every length \(2\le n\le30\). These finite checks are consistency tests; the all-\(n\) result follows from the proof above.

## Relationship to prior work
Eikmeier, Fleischmann, Kulczynski, and Nowotka introduced factor-weight equivalence and explicitly highlighted that, unlike the binary case, factor-weight-equivalent words can have different Parikh vectors. For the ternary standard measure they define the unique weighted prefix normal form; their example \(\mathtt{bcac}\mapsto\mathtt{cbbb}\) already attains the present bound at length \(4\).

Their conclusion states that the exact behavior of the weighted prefix normal form and of factor-weight-equivalent words, especially changes in Parikh vectors, remains open. The theorem here answers a sharp extremal version of that question for the smallest nonbinary standard alphabet.

Searches for the exact displacement formula, for ternary factor-weight-equivalent Parikh bounds, and for later work resolving the cited Parikh-vector question did not locate a covering result. The directly relevant indexed source remains the 2020 preprint and its 2021 proceedings version.

## Limitations
The proof uses the arithmetic progression of standard ternary weights in an essential way. It does not characterize whole equivalence classes, enumerate weighted prefix normal forms, or determine the corresponding extremal displacement for larger alphabets.

The originality search cannot exclude an unindexed note, thesis, or unpublished calculation phrased without weighted-prefix-normal terminology.

## References
1. Y. Eikmeier, P. Fleischmann, M. Kulczynski, and D. Nowotka, “Weighted Prefix Normal Words: Mind the Gap,” arXiv:2005.09281, first public version 2020-05-19.
2. Y. Eikmeier, P. Fleischmann, M. Kulczynski, and D. Nowotka, “Weighted Prefix Normal Words: Mind the Gap,” Developments in Language Theory 2021, Lecture Notes in Computer Science, DOI 10.1007/978-3-030-81508-0_12.
