# Quantitative density and sharp center resolution of neutral periodic fibers in heterochaos baker maps

## Finding
For every integer \(M\ge2\) and \(0<a<1/M\), every pair of a coarse base cylinder of depth \(r\ge0\) and a center \(M\)-adic cylinder of depth \(k\ge1\) contains a nontrivial vertical interval of points fixed by one and the same even iterate \(N\le2(r+k)\) of the generalized two-dimensional heterochaos baker map. The fiber derivative of that iterate equals one. In particular, the union of center-neutral periodic fibers is dense in the phase square. Conversely a maximal center-neutral periodic fiber interval contained in a depth-\(k\) center cylinder requires an even return iterate \(N\ge2k\); the latter center-resolution bound is attained for every prescribed center cylinder.

## Assumptions and scope
Use the half-open phase square \([0,1)^2\), with coordinates \((x,z)\). For \(i\in\{0,\ldots,M-1\}\), define push symbols \(i\) on the base interval \([ia,(i+1)a)\) by
\[
F_{a,M}(x,z)=\left(\frac{x-ia}{a},\frac{z+i}{M}\right).
\]
On \([Ma,1)\) use the pop symbol \(P\) with
\[
F_{a,M}(x,z)=\left(\frac{x-Ma}{1-Ma},\ Mz\bmod 1\right).
\]
The center pop uses the unique ordinary residue in \([0,1)\). Thus it has \(M\) affine pieces, as in the original generalized baker model. A base cylinder associated to a word \(u\) is the set of initial \(x\) whose first \(r\) base branch symbols form \(u\). A center \(M\)-adic cylinder associated to digits \(v\) of length \(k\) is the half-open interval with those first \(k\) base-\(M\) digits. By a *neutral periodic fiber component for \(F^N\)* we mean a maximal nondegenerate interval on a fixed vertical line, all of whose interior points are regular and fixed by \(F^N\), with center derivative \(1\). Return iterate \(N\) is not presumed primitive.

## Proof
Let \(D(z)=Mz\bmod1\) and \(P_i(z)=(z+i)/M\) for each push digit. The exact cancellation \(D\circ P_i=\mathrm{id}\) holds on the entire half-open unit interval.

Fix coarse base word \(u\) of length \(r\). Let \(c\) be its number of pushes and \(p\) its number of pops, so \(r=c+p\). Fix center digits \(v\) of length \(k\ge1\). Put
\[
h=\max(p,k),\qquad H=c-p+h\ge c,
\]
and choose any center word \(b\) of length \(h\) beginning with \(v\), e.g. extend \(v\) with \(h-k\) zero digits. Form the base word
\[
w=u\,P^H\,b^{\mathrm{rev}},
\]
where \(b^{\mathrm{rev}}\) is the sequence of the \(h\) push symbols in reverse order. The total number of pushes and pops in \(w\) both equal \(c+h\), and its length is
\[
N=r+H+h=2(c+h)\le2(r+k).
\]
Every base branch is a full-branch increasing affine bijection to \([0,1)\), with inverse slope \(a\) or \(1-Ma\), both strictly between zero and one. Consequently the inverse branches corresponding to \(w\) have a unique fixed point \(x_w\). The word \(w\) includes at least one push and at least one pop, so \(x_w\) is not an endpoint of any of its prescribed branch cylinders; hence it realizes \(w\) and is in the base cylinder for \(u\).

Let \(F_u^z\) denote the center composition along the coarse itinerary \(u\). By repeatedly canceling \(D\circ P_i\), the \(H\) added pops erase all \(c\) pushes and leave exactly \(h\) unmatched pops:
\[
D^H\circ F_u^z=D^h.
\]
The final reverse-ordered pushes prepend the digit block \(b\), and their composition is the digit-prefix map \(P_b\). Thus the complete center return map is exactly
\[
F_w^z=P_b\circ D^h.
\]
Write \(j=\sum_{q=1}^h b_qM^{h-q}\). On the \(M\)-adic interval
\[
I_b=[j/M^h,(j+1)/M^h)
\]
we have \(P_b(D^h z)=z\), so \(F^N(x_w,z)=(x_w,z)\) for all \(z\in I_b\). On its interior all center derivatives are defined; their product is \(M^hM^{-h}=1\). Since \(b\) extends \(v\), \(I_b\) lies in the prescribed center depth-\(k\) cylinder. Coarse base cylinders and center digit cylinders form a basis of the open square, establishing density.

For the lower bound, take any regular nondegenerate neutral fixed fiber for an iterate of length \(N\). On its fixed itinerary the center derivative is \(M^{p-c}\). Hence neutrality forces \(p=c=t\), so \(N=2t\). Repeated cancellation puts every such center word in reduced form \(P_b\circ D^h\) with \(0\le h\le t\); the maximal nondegenerate fixed fiber interval is one \(M\)-adic depth-\(h\) cylinder (the case \(h=0\) is the full unit interval). If this maximal fiber component is contained in a depth-\(k\) cylinder, its width \(M^{-h}\) cannot exceed \(M^{-k}\), so \(k\le h\le t=N/2\). Finally, given any word \(v\) of length \(k\), use the base word \(P^k v^{\mathrm{rev}}\) of length \(2k\): its center return is \(P_v\circ D^k\), and its maximal fixed interval is precisely the desired depth-\(k\) cylinder. Its base word is mixed and thus has the requisite regular periodic base point. This proves sharpness.

## Verification
The included standard-library script `verify_general_neutral_localization.py` implements the construction with exact rational arithmetic, replaying all prescribed base words through length \(3\) and center words through length \(3\) at three admissible rational parameters for each \(M\in\{2,3,4\}\). It independently checks both sample points inside each fixed fiber interval, the prefix containment, symbolic branch admissibility, and the stated period upper bound. The infinite-quantifier result is established by the preceding algebraic argument, not by these finite tests.

## Relationship to prior work
Saiki, Takahasi and Yorke (2018 preprint; 2021 journal) established density of both hyperbolic unstable-dimension classes for their original baker maps and noted one neutral period-two segment. Takahasi and Yamamoto (2022) defined the entire \(M\)-parameter generalized family and noted infinitely many periodic continua, but their main results concern Dyck coding and maximal-entropy measures. Takahasi (2024) studies distributions of hyperbolic periodic points separately. None of these examined full texts states the above **local center-cylinder localization with a uniform linear word-length period bound** or the sharp center-resolution lower bound. Broad categorical coding or aggregate counts of neutral components alone do not imply one exists inside *every* requested symbolic rectangle. The density is a new structural complement to the two hyperbolic dense classes, not a claim that neutral periodic intervals were previously unknown.

## Limitations
Regularity is asserted only for interiors of fiber intervals; branch boundaries need not be differentiable. Center-neutral points need not have least period \(N\). The sharp lower bound concerns depth of a **maximal** fixed fiber component, not an arbitrary subinterval and not the jointly prescribed base-and-center period upper bound. No density theorem is asserted here for three-dimensional invertible extensions. The same-model review does not establish independent certification or exhaustive publication priority.

## References
1. Y. Saiki, H. Takahasi, and J. A. Yorke, *Piecewise linear maps with heterogeneous chaos*, arXiv:1811.01009 (public November 2, 2018), Sections 1–3, https://arxiv.org/abs/1811.01009.
2. H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905 (public September 11, 2022), Sections 1–3, https://arxiv.org/abs/2209.04905.
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261 (public September 2, 2024), https://arxiv.org/abs/2409.01261.
