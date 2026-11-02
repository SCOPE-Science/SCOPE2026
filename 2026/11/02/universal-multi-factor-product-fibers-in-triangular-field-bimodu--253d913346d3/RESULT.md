# Universal multi-factor product fibers in triangular field-bimodule rings

## Finding
Let \(K,L\) be finite fields of the same characteristic, \(M\ne0\) a finite unital \((K,L)\)-bimodule, and \(R\) the triangular ring with entries \((a,v,c)\in K\times M\times L\) and multiplication
\[
(a,v,c)(d,w,f)=(ad,aw+vf,cf).
\]
Write \(Q=|K|\), \(T=|L|\), \(m=|M|\). Fix **any** integer \(k\ge1\), and let \(X_1,\ldots,X_k\) be independent, uniform elements of \(R\). Set
\[
t_Q=1-Q^{-1},\quad t_T=1-T^{-1},\quad
h_{Q,k}(x)=\begin{cases}1-t_Q^k,&x=0,\\ t_Q^k/(Q-1),&x\ne0,\end{cases}
\]
and define \(h_{T,k}\) analogously. Define the scalar
\[
E_k=\frac1{QT}\sum_{1\le i<j\le k}t_Q^{i-1}t_T^{k-j},
\]
where the empty sum is zero. For **every** target \((u,v,w)\in R\),
\[
\boxed{\Pr(X_1\cdots X_k=(u,v,w))
=\frac{h_{Q,k}(u)h_{T,k}(w)-E_k\mathbf1_{\{u=w=0\}}}{m}
+E_k\mathbf1_{\{u=w=0,\ v=0\}}.}
\]
Thus the **entire target-by-target product distribution for every word length** depends only on the three cardinalities \((Q,T,m)\), not on the left/right bimodule actions.

As a consequence, there exist two nonisomorphic rings of order \(256\) with identical \(k\)-fold product-fiber functions for **every** \(k\ge1\), yet centers of different sizes \(4\) and \(2\). In the equal-field case \(Q=T=q\) with \(m>1\), as \(k\to\infty\),
\[
\Pr(X_1\cdots X_k\ne0)\sim (1-m^{-1})\frac{k}{q}(1-q^{-1})^{k-1},
\]
and, conditional on a nonzero product, its distribution converges to the uniform distribution on the \(m-1\) nonzero strictly upper-triangular elements.

## Assumptions and scope
The bimodule is finite and nonzero, is unital on both sides, and its left \(K\)- and right \(L\)-actions commute. No symmetry or faithfulness beyond those automatic field-module properties is assumed. Since both fields act unitaly on the same finite additive group, they have a common prime characteristic. Both field sizes are at least two; \(m>1\). The random factors are independent and uniformly distributed. Zero in \(K,L,M\) is denoted by the same symbol when unambiguous. Every statement holds in all positive characteristics and includes word length one.

## Proof
**1. Diagonal factors.** The diagonal coordinate of a \(k\)-fold product is the product of \(k\) independent uniform field elements. It vanishes with probability \(1-(1-Q^{-1})^k\). Conditional on nonvanishing, its value is uniform in \(K^\times\), since multiplication by an independent uniform nonzero factor is transitive. Hence its exact target mass is \(h_{Q,k}\). The other diagonal has mass \(h_{T,k}\), independently, since all diagonal coordinates in all factors are independent.

**2. Off-diagonal coefficients.** Write \(X_i=(a_i,b_i,c_i)\). Repeated multiplication, proved by induction, yields
\[
(X_1\cdots X_k)_{12}
=\sum_{j=1}^k(a_1\cdots a_{j-1})b_j(c_{j+1}\cdots c_k).
\]
An empty product is the corresponding unit. The \(b_j\) are mutually independent and uniform on \(M\), also independent of all diagonals. For each \(j\), its additive coefficient map is zero if either scalar product is zero, and is an invertible additive map if both products are nonzero: indeed multiplication by any nonzero field element is invertible on the appropriate side of a unital module. Therefore, conditional on all diagonals, the off-diagonal output is uniformly distributed over \(M\) whenever one coefficient is invertible, and is identically zero when all coefficients vanish.

**3. Probability that every coefficient vanishes.** Let \(\alpha\) be the first index with \(a_\alpha=0\), with \(\alpha=k+1\) if none exists. Let \(\gamma\) be the last index with \(c_\gamma=0\), with \(\gamma=0\) if none exists. The coefficient indexed by \(j\) is invertible precisely when \(j\le\alpha\) and \(j\ge\gamma\). Thus all coefficients vanish exactly when \(\alpha<\gamma\). This event forces *both* diagonal products to vanish. For any \(1\le i<j\le k\), independence yields
\[
\Pr(\alpha=i,\gamma=j)
=\frac1Q\,t_Q^{i-1}\cdot\frac1T\,t_T^{k-j}.
\]
Summing these disjoint cases gives exactly \(E_k\).

**4. Complete fibers.** At a target with at least one nonzero diagonal, the conditional off-diagonal distribution is uniform, giving the first term with \(E_k=0\). When both target diagonals vanish, the diagonal event has mass \(h_{Q,k}(0)h_{T,k}(0)\). Of that mass, \(E_k\) is concentrated at off-diagonal zero, and the remaining mass is uniform over \(M\). This yields the displayed unified formula, proving the theorem for all \(Q,T,m,k\).

**5. Nonisomorphic 256-element pair.** Put \(F=\mathbb F_4\), \(K=L=F\), and \(M=F\oplus F\) with the usual left action. In one ring, let the right action be \((v_1,v_2)c=(v_1c,v_2c)\); in the other, let it be \((v_1,v_2)c=(v_1c,v_2c^2)\). Frobenius is an automorphism, so both are unital bimodules. Both rings have \(4\cdot16\cdot4=256\) elements and the same \((Q,T,m)\), hence their entire product distributions coincide for every \(k\). Commutation with \((1,0,0)\) forces the off-diagonal entry of every central element to be zero. Centrality of \((a,0,c)\) is then precisely the condition \(av=vc\) for all \(v\in M\). In the first ring this says \(a=c\in F\), yielding four central elements. In the second ring it says \(a=c=c^2\), so \(a=c\in\mathbb F_2\), yielding two. The centers have different sizes; the rings cannot be isomorphic.

**6. Equal-field asymptotic.** For \(Q=T=q\) let \(t=1-q^{-1}\). Evaluating the arithmetic-geometric sum gives
\[
E_k=q^{-2}\sum_{j=0}^{k-2}(j+1)t^j
=1-kt^{k-1}+(k-1)t^k
\quad(k\ge1),
\]
with an empty sum at \(k=1\). The total mass on nonzero strictly upper-triangular targets is \((1-m^{-1})[(1-t^k)^2-E_k]\). The bracket is asymptotic to \(kq^{-1}t^{k-1}\); the probability that either diagonal of the product is nonzero is \(1-(1-t^k)^2=O(t^k)\), lower by a factor of order \(k\). It follows that the former class accounts asymptotically for all nonzero products and its individual masses are exactly equal. This proves both asymptotic assertions. \(\square\)

## Verification
The accompanying standalone `verify_prime_fields.py` computes the full \(k\)-fold product distribution by successive exact convolution on all elements of \(T_2(\mathbb F_q)\) for \(q=2,3\), \(1\le k\le5\), and \(q=5\), \(1\le k\le3\), comparing every target against the formula. The independent `verify_bimodule.py` uses explicit four-element-field arithmetic, testing the asymmetric bimodule \((K,L,M)=(\mathbb F_2,\mathbb F_4,\mathbb F_4)\) through word length four, and both the ordinary and Frobenius-twisted \((\mathbb F_4,\mathbb F_4,\mathbb F_4^2)\) bimodules through word length three, at every target. Both end in `VERIFY_OK`; their exact outputs are included. The derivation above, not these finite tests, establishes the infinite parameter range.

## Relationship to prior work
Dolžan (2025) studies the distribution of **two** unrestricted factors in finite rings; the earlier two-factor triangular field-bimodule formula is acknowledged as an exact \(k=2\) specialization of the present result and is not claimed as new. Sarma and Subedi (2026) study the **aggregate event** that a two-factor product is nilpotent, including its triangular-matrix diagonal reduction. Sarma and Subedi (2025) investigate zero-products of \(k\) factors and prove bounds, with a principal focus on commutative rings; their results do not specify every target of a noncommutative triangular bimodule ring. The contribution here is the **all-length target-fiber law** with arbitrary compatible bimodule actions, including the stronger all-length indistinguishability of the nonisomorphic 256-element pair and the equal-field rare-event limit. All earlier two-factor and aggregate-probability results remain credited to their original sources.

## Limitations
The theorem assumes finite *fields* on both diagonal blocks and a finite unital bimodule. It does not cover general local diagonal rings, non-independent factor sampling, rectangular chains with more than two diagonal blocks, or arbitrary finite rings. It does not assert that the displayed 256-element pair has minimum possible order among all all-length-indistinguishable nonisomorphic pairs. Earlier general semigroup convolution theory could conceivably imply the formula; historical priority has not been independently certified.

## References
1. D. Dolžan, *The multiplication probability of a finite ring*, arXiv:2504.12886v1, first public April 17, 2025; especially Sections 2–4 on two-factor product distributions.
2. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1, first public October 6, 2026; especially Section 2.3 on triangular matrices.
3. D. Sarma and T. Subedi, *The probability that the product of \(k\) elements in a finite ring is zero*, arXiv:2506.10392v1, first public June 12, 2025; especially Sections 1–2 on all-length zero-product bounds.
