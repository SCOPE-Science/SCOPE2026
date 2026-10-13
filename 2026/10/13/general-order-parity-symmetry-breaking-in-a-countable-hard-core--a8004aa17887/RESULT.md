# General-order parity symmetry breaking in a countable hard-core Cayley-tree operator
## Finding
For the countable-state hard-core Cayley-tree operator of Olimov--Rozikov with adjacency pattern (4.1), keep the source's equal parity activity totals \(L_1=L_2=L>0\), but allow every integer tree order \(k\ge2\). Write \(\ell=\lambda_1>0\), \(M_1=\sum_{j\ge1}x_{2j+1}\), and \(M_2=\sum_{j\ge1}x_{2j}\). Every nonsymmetric positive mass solution is, up to interchanging \(M_1,M_2\), uniquely parameterized by \(s>0\) as
\[
M_1=e^{ks}\frac{\sinh s}{\sinh((k-1)s)},\qquad
M_2=e^{-ks}\frac{\sinh s}{\sinh((k-1)s)},
\]
and exists exactly at
\[
L=\Lambda_{k,\ell}(s):=
\frac{\sinh s\,[\ell\sinh((k-1)s)+\sinh((k+1)s)]^k}
{\sinh((k-1)s)\,\sinh^k(ks)}.
\]
The nonsymmetric branch meets the symmetric point at
\[
L_c(k,\ell)=\frac{((k-1)\ell+k+1)^k}{k^k(k-1)}.
\]
Moreover,
\[
\log\frac{\Lambda_{k,\ell}(s)}{L_c(k,\ell)}=
\frac{k((k+1)(k+3)-3\ell(k-1)^2)}{6((k-1)\ell+k+1)}s^2+O(s^4).
\]
Hence if \(\ell>(k+1)(k+3)/(3(k-1)^2)\), then \(\Lambda_{k,\ell}\) initially decreases below \(L_c\), while \(\Lambda_{k,\ell}(s)\to\infty\) as \(s\to\infty\). Consequently its global minimum \(L_{\min}(k,\ell)\) satisfies \(L_{\min}<L_c\), and for every \(L\in(L_{\min},L_c)\) there are at least two distinct positive parameters \(s\), hence two swapped pairs of nonsymmetric fixed points, together with at least one symmetric fixed point. Therefore the source operator has at least five fixed points, and thus at least five normalisable boundary laws and translation-invariant Gibbs measures, throughout that nonempty interval. For \(k=2\), \(L_c=(\ell+3)^2/4\) and the parameterization reduces to the source relation \(M_1M_2=1\).

## Assumptions and scope
Fix an integer \(k\ge2\). Consider the positive \(\ell^1\) operator introduced by Olimov and Rozikov for the hard-core graph whose adjacency matrix has \(a_{11}=1\), \(a_{1j}=1\), \(a_{i1}=0\) for \(i\ne1\), and, for \(i,j\ne1\), \(a_{ij}=1\) exactly when \(i+j\) is even. Let the activity sequence be positive and summable. Put \(\ell=\lambda_1\), \(L_1=\sum_{j\ge1}\lambda_{2j+1}\), and \(L_2=\sum_{j\ge1}\lambda_{2j}\), and impose the source specialization \(L_1=L_2=L\).

For a fixed point, put \(M_1=\sum_{j\ge1}x_{2j+1}\), \(M_2=\sum_{j\ge1}x_{2j}\), and \(D=1+\ell+M_1+M_2\). The source's general-order operator then reduces exactly to
\[
M_1=L\left(\frac{1+M_1}{D}\right)^k,\qquad
M_2=L\left(\frac{1+M_2}{D}\right)^k.
\]
The finding classifies the nonsymmetric solutions of this two-mass reduction and proves a nonempty parameter region with at least five fixed points. It does not claim that five is the global maximum for \(k>2\).

## Proof
Assume first that \(M_1>M_2\) and set
\[
r=\left(\frac{M_1}{M_2}\right)^{1/k}>1.
\]
Dividing the two mass equations gives
\[
r=\frac{1+M_1}{1+M_2}.
\]
Combining this with \(M_1=r^kM_2\) yields reversibly
\[
M_2=\frac{r-1}{r^k-r},\qquad M_1=\frac{r^k(r-1)}{r^k-r}.
\]
Writing \(r=e^{2s}\), \(s>0\), gives
\[
M_1=e^{ks}\frac{\sinh s}{\sinh((k-1)s)},\qquad
M_2=e^{-ks}\frac{\sinh s}{\sinh((k-1)s)}.
\]
Thus every nonsymmetric solution produces exactly one \(s>0\), up to the interchange \(M_1\leftrightarrow M_2\); conversely these formulas satisfy the ratio equation for every \(s>0\).

Two elementary hyperbolic identities give
\[
D=\ell+\frac{\sinh((k+1)s)}{\sinh((k-1)s)},\qquad
1+M_1=e^s\frac{\sinh(ks)}{\sinh((k-1)s)}.
\]
Substitution into the first mass equation therefore gives exactly
\[
L=\Lambda_{k,\ell}(s)=
\frac{\sinh s\,[\ell\sinh((k-1)s)+\sinh((k+1)s)]^k}
{\sinh((k-1)s)\,\sinh^k(ks)}.
\]
This proves both necessity and sufficiency of the parameterization.

Taking \(s\downarrow0\) gives \(M_1,M_2\to1/(k-1)\) and
\[
L_c(k,\ell)=\frac{((k-1)\ell+k+1)^k}{k^k(k-1)}.
\]
Using \(\log(\sinh(as))=\log(as)+a^2s^2/6+O(s^4)\) and expanding the mixed numerator gives
\[
\log\frac{\Lambda_{k,\ell}(s)}{L_c(k,\ell)}=
\frac{k((k+1)(k+3)-3\ell(k-1)^2)}{6((k-1)\ell+k+1)}s^2+O(s^4).
\]
Hence for
\[
\ell>\frac{(k+1)(k+3)}{3(k-1)^2},
\]
there is \(s_0>0\) with \(\Lambda_{k,\ell}(s_0)<L_c\). On the other hand, direct use of \(\sinh(as)\sim e^{as}/2\) gives \(\Lambda_{k,\ell}(s)\sim e^{2s}\), so the branch diverges to infinity. Continuity therefore gives a global minimum \(L_{\min}<L_c\). For every \(L\) strictly between these values, the intermediate value theorem gives one solution parameter before a minimizer and another after it. Each parameter gives two ordered nonsymmetric mass pairs by swapping the parities.

Finally, the symmetric equation
\[
M=L\left(\frac{1+M}{1+\ell+2M}\right)^k
\]
has at least one positive solution for every \(L>0\): the right side minus \(M\) is positive at \(M=0\) and tends to negative infinity as \(M\to\infty\). Thus the stated interval contains at least four nonsymmetric fixed points plus at least one symmetric fixed point. The source proves that these positive fixed points give normalisable boundary laws and translation-invariant Gibbs measures.

For \(k=2\), the formulas give \(M_1M_2=1\) and \(L_c=(\ell+3)^2/4\), recovering the algebraic merger in the source's binary-tree section.

## Verification
The accompanying `verify_parity_branch.py` reconstructs the mass equations from the displayed parameterization for orders \(2\) through \(12\), checks representative positive \(s\)-values, verifies the downward local bend above the stated \(\ell\)-threshold, exhibits two crossings of an intermediate level below \(L_c\), and checks the \(k=2\) specialization. It reports `VERIFY_OK`. These finite checks are corroborative only; the proof above is analytic for every integer \(k\ge2\).

## Relationship to prior work
Olimov and Rozikov define the operator for arbitrary Cayley order \(k\), but their non-uniqueness section explicitly sets \(k=2\). For the parity adjacency pattern they introduce \(M_1,M_2,L_1,L_2\), then impose \(L_1=L_2\), obtain the binary-tree mass equations, and classify a regime with up to five fixed points. The present result keeps exactly that graph and equal-parity specialization while solving the nonsymmetric mass branch for every \(k\ge2\).

A closely related countable-state hard-core paper by Rozikov and Haydarov studies a different model on spin space \(\mathbb Z\) through a scalar dynamical system and constructs an uncountable family of Gibbs measures. Its inspected abstract does not contain the parity adjacency reduction or the all-order parameterization proved here. Later work on weakly periodic or translation-invariant countable-state hard-core models uses different reductions; no inspected statement implies the displayed \(\Lambda_{k,\ell}\) law or the five-fixed-point interval for this source graph.

## Limitations
The theorem is restricted to the source adjacency pattern and to equal parity activity totals \(L_1=L_2\). It gives a sufficient nonempty region with at least five fixed points when \(\ell>(k+1)(k+3)/(3(k-1)^2)\); it does not classify all symmetric roots, all possible nonsymmetric branch turns, or the exact total number of fixed points for \(k>2\). It does not address extremality, reconstruction, free energy, or non-translation-invariant Gibbs measures. An equivalent reduction could exist in weakly indexed follow-up literature under different variables.

## References
1. U. R. Olimov and U. A. Rozikov, *Fixed points of an infinite-dimensional operator related to Gibbs measures*, Theoretical and Mathematical Physics 214 (2023), 282--295. arXiv:2206.13822v1; DOI:10.1134/S0040577923020125.
2. U. A. Rozikov and F. H. Haydarov, *A HC model with countable set of spin values: Uncountable set of Gibbs measures*, Reviews in Mathematical Physics 35 (2023), 2250039. arXiv:2206.06333; DOI:10.1142/S0129055X22500398.
