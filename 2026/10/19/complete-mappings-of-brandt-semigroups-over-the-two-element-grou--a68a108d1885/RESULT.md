# Complete mappings of Brandt semigroups over the two-element group

## Finding
For each integer \(n\ge1\), let \(I\) have \(n\) elements and let \(B_n(C_2)\) be the Brandt semigroup over \(C_2=\mathbb Z/2\mathbb Z\), with zero. A *complete mapping* is a bijection \(\alpha:B_n(C_2)\to B_n(C_2)\) for which \(x\mapsto x\alpha(x)\) is also a bijection.

If \(n=2t\) is even, identify \(I=C_2\times\mathbb Z/t\mathbb Z\). For \(a,b,g\in C_2\) and \(u,v\in\mathbb Z/t\mathbb Z\), the formula
\[
\alpha(0)=0,\qquad
\alpha\bigl(((a,u),g,(b,v))\bigr)
=\bigl((b,v),a+b+g,(g,u+v)\bigr)
\]
is a complete mapping. If \(n\) is odd there is no complete mapping.

Moreover, **the nine-element semigroup \(B_2(C_2)\) has exactly 32 complete mappings**. The parity-based existence criterion is also a consequence of the published inverse-semigroup theorem; the explicit uniform formula and the exact nine-element count are the asserted contributions.

## Assumptions and scope
Write \(S=B_n(C_2)=(I\times C_2\times I)\cup\{0\}\). The zero element annihilates every element. The remaining products are
\[
(i,g,j)(k,h,\ell)=
\begin{cases}
(i,g+h,\ell)&\text{if }j=k,\\
0&\text{if }j\ne k.
\end{cases}
\]
All additions in the middle coordinate are modulo two. The index-set identification for even \(n\) uses addition modulo \(t\) in its second component; it also works when \(t=1\). All mappings counted are permutations of the full labeled set \(S\), with the zero element included. The claim makes no enumeration assertion for larger even \(n\).

## Proof
**Normal form.** Let \(\alpha\) be a complete mapping, and put \(\theta(x)=x\alpha(x)\). Since \(\theta(0)=0\) and \(\theta\) is injective, every nonzero input has a nonzero product. Therefore there are unique \(h,k\) with
\[
\alpha(i,g,j)=(j,h,k).
\]
Because \(\alpha\) is bijective, it fixes zero. For each fixed \(j\), its restriction is a permutation
\[
F_j:I\times C_2\longrightarrow C_2\times I,
\quad (i,g)\longmapsto(h,k).
\]
Because \(\theta(i,g,j)=(i,g+h,k)\) is bijective, for each fixed \(i\) the map \((g,j)\mapsto(g+h,k)\) is a permutation of \(C_2\times I\).

**Parity necessity.** Sum the group coordinates modulo two. Across all \(j\), each \(F_j\) has exactly \(n\) outputs with \(h=1\), so \(\sum h\equiv n^2\pmod2\). Across all \(i\), the same argument for \(\theta\) gives \(\sum(g+h)\equiv n^2\pmod2\). There are exactly \(n^2\) original inputs with \(g=1\), giving \(\sum g\equiv n^2\pmod2\). Consequently \(n^2\equiv n^2+n^2\equiv0\pmod2\), and \(n\) is even.

**Explicit sufficiency.** Suppose \(n=2t\), with \(I=C_2\times\mathbb Z/t\mathbb Z\). For fixed \(j=(b,v)\), the nonzero part of \(\alpha\) sends the source pair \(((a,u),g)\) to \((a+b+g,(g,u+v))\). This is a bijection: from the output one recovers \(g\), then \(u\), then \(a\). Hence \(\alpha\) is bijective. Its associated product is
\[
\theta\bigl(((a,u),g,(b,v))\bigr)=
\bigl((a,u),a+b,(g,u+v)\bigr).
\]
For each fixed \(i=(a,u)\), one recovers \(b\) from the output middle coordinate, \(g\) from the first component of the right index, and \(v\) from its second component. Therefore \(\theta\) is bijective as well. Both maps fix zero.

**Exact count at \(n=2\).** Take \(I=\{0,1\}\). For either fixed \(j\), a permissible \(F_j:(i,g)\mapsto(h,k)\) must have distinct output indices \(k\) on the two inputs \((i,0)\) and \((i,1)\). Indeed, if those indices coincided, injectivity of \(F_j\) would force the two output \(h\)-bits to differ, making the two \(\theta\)-images equal. There are precisely \(2^2\) choices of the bijections \(g\mapsto k\), one for each \(i\). Once these are chosen, for each \(k\) the two values of \(h\) across \(i=0,1\) must be distinct; this gives \(2^2\) further choices. Thus there are exactly \(16\) possible first blocks \(F_0\).

Fix one such \(F_0\). At fixed \((i,k)\), denote by \(g_0(i,k)\) the unique input bit reaching \(k\), and by \(h_0(i,k)\) the corresponding output bit. The second block must use a bijection \(k\mapsto g_1(i,k)\) for each \(i\), giving a bit \(e_i\in C_2\) with \(g_1(i,k)=g_0(i,k)+e_i\). The two \(\theta\)-output bits at this \((i,k)\) must be complementary, forcing
\[
h_1(i,k)=1+h_0(i,k)+e_i.
\]
For each fixed \(k\), the two \(h_0(i,k)\) values are distinct. The two \(h_1(i,k)\) values are distinct exactly when \(e_0=e_1\). There are therefore two possible second blocks for each first block, all satisfying both bijections. The total is \(16\cdot2=32\).

## Verification
The accompanying standalone Python 3 file `verify.py` uses two independent finite enumerations. One enumerates the \(24^2\) pairs of local permutations, pruning impossible first blocks, and obtains \(16\) possible first blocks, each with \(2\) followers. The second exhaustively checks all \(8!\) permutations of the eight nonzero elements, obtaining exactly \(32\). It also constructs and verifies the displayed mapping for \(n=2,4,6,8,10\). The mathematical proof above is valid for all even indices and does not depend on these finite tests.

To reproduce, run `python3 verify.py` from the directory containing this report and `verify.py`.

## Relationship to prior work
Araújo, Bentz, Cameron, Hendrey and Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092 (2026), establish the general existence criterion for finite inverse semigroups (Theorem 10.1); specialized to \(B_n(C_2)\), that criterion already gives existence exactly for even \(n\). Their Proposition 6.5 counts complete mappings of the *combinatorial* Brandt semigroup \(B_n\), whose maximal subgroup is trivial, via Latin squares. In particular they report \(2\) for the five-element \(B_2\); this does not count the nine-element \(B_2(C_2)\). The present explicit coordinate formula for every even \(n\) and the count \(32\) for the first admissible Brandt example over \(C_2\) are separate from those conclusions. Kinyon's June 2025 lecture slides provide earlier public background for the existence problem and the five-element example.

## Limitations
The total count is determined only for the first admissible index over the two-element group, not all even indices. Other explicit constructions might be equivalent under relabeling; classification modulo automorphisms is not claimed. The earlier existence criterion must not be considered novel. The numerical count is independently reproduced by finite exhaustive enumeration; the general parity and construction assertions have proofs above. Possible earlier equivalent constructions or counts in unindexed semigroup-transversal literature remain a residual originality risk.

## References
1. J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1, 25 August 2026. https://arxiv.org/abs/2608.25092 (especially Proposition 6.5, Corollary 7.6, Theorem 10.1).
2. M. Kinyon, *Complete Mappings for Semigroups*, public lecture slides, AGTA, University of Naples Federico II, 24 June 2025. https://www.advgrouptheory.com/agta2025/Talks/Kinyon.pdf.
