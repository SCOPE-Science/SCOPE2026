# All-order parity-breaking fixed points of a countable positive operator

## Finding

Consider the positive operator
\[
 F_i(x)=\lambda_i\left(\frac{1+\sum_{j\ge1}a_{ij}x_j}{1+\sum_{j\ge1}x_j}\right)^k,\qquad i\ge1,
\]
with the array printed in (4.1) of Olimov–Rozikov [1]: \(a_{1j}=1\) for all \(j\), \(a_{i1}=0\) for \(i\ge2\), and \(a_{ij}=\mathbf 1_{i+j\text{ even}}\) for \(i,j\ge2\). Let \(k\ge2\) be an integer and \((\lambda_i)\) a strictly positive summable sequence. Write
\[
 \ell=\lambda_1>0,\qquad L=\sum_{j\ge1}\lambda_{2j+1}=\sum_{j\ge1}\lambda_{2j}>0.
\]
For a fixed point \(x\), put \(M_1=\sum_{j\ge1}x_{2j+1}\), \(M_2=\sum_{j\ge1}x_{2j}\). Every unequal ordered mass solution, up to swapping its two components, is uniquely represented by \(s>0\) via
\[
 M_1=e^{ks}\frac{\sinh s}{\sinh((k-1)s)},\qquad
 M_2=e^{-ks}\frac{\sinh s}{\sinh((k-1)s)},
\]
and these masses give a fixed point exactly when
\[
 L=\Lambda_{k,\ell}(s):=\frac{\sinh s\,[\ell\sinh((k-1)s)+\sinh((k+1)s)]^k}{\sinh((k-1)s)\,\sinh^k(ks)}.
\]
The branch meets the equal-mass point \(M_1=M_2=1/(k-1)\) at
\[
 L_c(k,\ell)=\frac{((k-1)\ell+k+1)^k}{k^k(k-1)}.
\]
Its local bend is
\[
 \log\frac{\Lambda_{k,\ell}(s)}{L_c(k,\ell)}=\frac{k((k+1)(k+3)-3\ell(k-1)^2)}{6((k-1)\ell+k+1)}s^2+O(s^4).
\]
If \(\ell>(k+1)(k+3)/(3(k-1)^2)\), then \(\Lambda_{k,\ell}\) attains a minimum \(L_{\min}(k,\ell)<L_c(k,\ell)\) at some \(s>0\). For every \(L\in(L_{\min},L_c)\), the operator has at least five distinct positive summable fixed points: at least four with unequal masses and at least one with equal masses.

## Assumptions and scope

This is a fixed-point result for the array as printed, not a Gibbs-measure result. The array is nonsymmetric: \(a_{1j}=1\) and \(a_{j1}=0\) for \(j>1\). It therefore cannot be the adjacency matrix of the undirected graph used in the Gibbs formalism of [1, §5]. The swap is a symmetry of the reduced equations under equality of the activity totals; it need not be a sitewise parity symmetry of the activity sequence. No exact count or upper bound is asserted for \(k>2\).

## Proof

The operator maps positive summable vectors to positive summable vectors since \(0<F_i(x)\le\lambda_i\). Its first component is identically \(\ell\). Writing \(D=1+\ell+M_1+M_2\), a fixed point thus satisfies
\[
 M_p=L\left(\frac{1+M_p}{D}\right)^k,\qquad p=1,2.
\]
Conversely every positive solution of these two equations uniquely gives a fixed point: take \(x_1=\ell\) and \(x_i=\lambda_i M_p/L\) in parity block \(p\). This vector has the prescribed masses and is summable, and the two mass equations verify its coordinate equations. Distinct ordered mass pairs give distinct vectors.

Suppose \(M_1>M_2\), and put \(r=(M_1/M_2)^{1/k}>1\). Division gives \(r=(1+M_1)/(1+M_2)\), hence
\[
 M_2=\frac{r-1}{r^k-r},\qquad M_1=\frac{r^k(r-1)}{r^k-r}.
\]
With \(r=e^{2s}\) these are the claimed formulas. The identities
\[
 1+M_1+M_2=\frac{\sinh((k+1)s)}{\sinh((k-1)s)},\qquad
 1+M_1=e^s\frac{\sinh(ks)}{\sinh((k-1)s)}
\]
reduce the first mass equation to \(L=\Lambda_{k,\ell}(s)\). The ratio relation then supplies the second mass equation. This proves the stated necessity, sufficiency and uniqueness of the parameter.

As \(s\downarrow0\) the masses tend to \(1/(k-1)\), a solution of the equal-mass equations at \(L=L_c\). Put \(A=(k-1)\ell+k+1\). After expanding \(\sinh(as)=as(1+a^2s^2/6+O(s^4))\), six times the quadratic coefficient in the logarithm is
\[
 1-(k-1)^2-k^3+k\frac{\ell(k-1)^3+(k+1)^3}{A},
\]
which reduces to the formula in the finding. At infinity the dominant exponent in \(\Lambda\) is \(1+k(k+1)-(k-1)-k^2=2\), with prefactor one. Thus under the stated threshold the continuous branch initially falls below \(L_c\) and eventually exceeds any finite level. It has a global minimum at a positive finite \(s\), and for each intermediate level \(L\) there is one crossing on each side of a minimizer by the intermediate value theorem. The two distinct parameters and their mass swaps furnish four fixed points. Finally, \(L[(1+M)/(1+\ell+2M)]^k-M\) is positive at zero and tends to minus infinity, so an additional equal-mass fixed point exists.

## Verification and relation to prior work

The reversible reduction, Taylor expansion and intermediate value argument are valid for every integer \(k\ge2\). The accompanying `verify_parity_branch.py` is a finite corroboration of the mass equations, local bend and branch crossings; it is not a proof of the all-order result. At \(k=2\) our formulas reduce to \(M_1M_2=1\) and \(L_c=(\ell+3)^2/4\), recovering the merger in [1, §4]. The general operator in [1] allows arbitrary \(k\), but the parity nonuniqueness analysis there sets \(k=2\). The new conclusion concerns its all-order formal fixed points. The distinct countable-state model of [2] uses a different reduction. The present result does not address unequal activity totals, extremality, or compatibility of a directed array with a Gibbs specification.

## References

1. U. R. Olimov and U. A. Rozikov, *Fixed points of an infinite-dimensional operator related to Gibbs measures*, Theoretical and Mathematical Physics 214 (2023), 282–295. arXiv:2206.13822v1; DOI:10.1134/S0040577923020125.
2. U. A. Rozikov and F. H. Haydarov, *A HC model with countable set of spin values: Uncountable set of Gibbs measures*, Reviews in Mathematical Physics 35 (2023), 2250039. arXiv:2206.06333; DOI:10.1142/S0129055X22500398.
