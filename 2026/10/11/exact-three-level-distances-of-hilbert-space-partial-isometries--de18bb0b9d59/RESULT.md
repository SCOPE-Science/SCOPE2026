# Exact three-level distances of Hilbert-space partial isometries to absolutely norm-attaining operators

## Finding

Let \(H\) be a separable infinite-dimensional complex Hilbert space and let \(\mathcal{AN}(H)\) denote the bounded linear operators on \(H\) whose restriction to every nonzero closed subspace attains its operator norm. For each partial isometry \(W\in\mathcal B(H)\), put

\[
d(W)=\inf_{S\in\mathcal{AN}(H)}\|W-S\|.
\]

Then

\[
d(W)=
\begin{cases}
0,&\operatorname{rank}W<\infty\ \text{or}\ \dim\ker W<\infty,\\[2pt]
\tfrac12,&\operatorname{rank}W=\dim\ker W=\dim\ker W^*=\infty,\\[2pt]
1,&\operatorname{rank}W=\dim\ker W=\infty,\ \dim\ker W^*<\infty.
\end{cases}
\]

The same distances hold with the norm closure of \(\mathcal{AN}(H)\) in place of \(\mathcal{AN}(H)\), and every infimum above is attained in \(\mathcal{AN}(H)\). In particular, the value cannot be recovered from the modulus \(|W|=(W^*W)^{1/2}\) alone.

## Assumptions and scope

The scalar field is complex. The separability assumption is used only to identify two infinite-dimensional orthogonal summands by a unitary. A partial isometry is zero on its kernel and isometric on its initial space. Write \(N=\ker W\), \(M=N^\perp\), and \(R=\operatorname{ran}W\); its final space \(R\) is closed, and \(\ker W^*=R^\perp\). Distances use the full operator norm on \(\mathcal B(H)\). Finite and infinite dimensions in the displayed cases refer to algebraic Hilbert-space dimensions.

We use the following published structural characterization, not a claim of the present result: if \(S\in\overline{\mathcal{AN}(H)}\) is noncompact, its modulus satisfies \(|S|=\alpha I+K\), where \(\alpha>0\) and \(K\) is compact self-adjoint; furthermore \(\dim\ker S<\infty\). This is Theorem 3.7 and Corollary 3.8 of Ramesh–Sequeira (2022).

## Proof

**First case.** If \(W\) has finite rank, it is compact, and every restriction to a nonzero closed subspace attains its norm: its image of the weakly compact unit ball has a norm-maximizing point. If \(\dim N<\infty\), every infinite-dimensional closed subspace of \(H\) contains a unit vector in \(M\), so \(W\) attains norm one on that subspace; every finite-dimensional subspace has a compact unit sphere. Thus \(W\in\mathcal{AN}(H)\) in either event and \(d(W)=0\).

**Universal lower bound for infinite initial space and kernel.** Assume \(\dim M=\dim N=\infty\). Fix \(S\in\overline{\mathcal{AN}(H)}\). If \(S\) is compact, take an orthonormal sequence \((f_j)\subset M\). Since \(Sf_j\to0\) and \(\|Wf_j\|=1\), necessarily \(\|W-S\|\ge1\). If \(S\) is noncompact, its structural representation above gives \(|S|=\alpha I+K\), \(\alpha>0\), with \(K\) compact. For orthonormal sequences \((e_j)\subset N\) and \((f_j)\subset M\), compactness yields

\[
\|Se_j\|=\||S|e_j\|\longrightarrow\alpha,
\qquad
\|Sf_j\|=\||S|f_j\|\longrightarrow\alpha.
\]

Because \(We_j=0\) and \(\|Wf_j\|=1\), the reverse triangle inequality gives

\[
\|W-S\|\ge\max\{\alpha,|1-\alpha|\}\ge\tfrac12.
\]

Thus \(d(W)\ge1/2\) whenever both the initial space and kernel are infinite-dimensional.

**Infinite cokernel attains one half.** Suppose in addition \(\dim R^\perp=\infty\). Separability supplies a unitary map \(V:N\to R^\perp\). Define \(U\) on the orthogonal decomposition \(H=M\oplus N\) by \(U|_M=W|_M\) and \(U|_N=V\). Its images are orthogonal and exhaust \(H\), so \(U\) is unitary. The operator \(S=U/2\) is absolutely norm attaining, since it is a scalar multiple of an isometry. On \(M\), \(W-S=U/2\); on \(N\), \(W-S=-U/2\), whence \(\|W-S\|=1/2\). This matches the lower bound.

**Finite cokernel forces distance one.** Suppose instead \(\dim R^\perp<\infty\). Let \(S\in\overline{\mathcal{AN}(H)}\) satisfy \(\delta=\|W-S\|<1\). The map \(A=P_RS|_M:M\to R\) satisfies \(\|A-W|_M\|\le\delta\). As \(W|_M:M\to R\) is unitary, the Neumann-series criterion shows that \(A\) is invertible. For each \(x\in N\), set \(y_x=-A^{-1}P_R Sx\in M\) and \(g_x=x+y_x\). The map \(x\mapsto g_x\) is injective, hence its image \(G\) is infinite-dimensional, while

\[
P_R Sg_x=P_R Sx+A y_x=0,
\qquad S(G)\subseteq R^\perp.
\]

Since \(R^\perp\) is finite-dimensional, \(S|_G\) has infinite-dimensional kernel, and so \(\dim\ker S=\infty\). This contradicts the published finite-kernel property if \(S\) is noncompact; if \(S\) is compact, the preceding orthonormal-sequence argument independently gives \(\|W-S\|\ge1\). Thus no \(S\) in the closure lies within distance less than one. As the zero operator belongs to \(\mathcal{AN}(H)\) and \(\|W\|=1\), the distance is exactly one.

**Same-modulus separation.** On \(\ell_2(\mathbb N)\), let \(P\) be the orthogonal projection onto the odd-coordinate subspace. Set \(Ce_{2j-1}=e_j\) and \(Ce_{2j}=0\) for all \(j\ge1\). Both are partial isometries with \(|P|=|C|=P\); the kernel, range, and cokernel of \(P\) are respectively infinite, infinite, infinite, whereas \(C\) is onto and has infinite kernel and rank. Therefore \(d(P)=1/2\) and \(d(C)=1\).

Finally, distance to a set equals distance to its norm closure, so all formulae remain true for \(\overline{\mathcal{AN}(H)}\). The exhibited approximants belong to the nonclosed class itself.

## Verification

The proof uses no numerical computations and does not infer any infinite-dimensional assertion from finite truncation. Its externally dependent input is the exact modulus-plus-compact and finite-kernel conclusion in Ramesh–Sequeira, Theorem 3.7 and Corollary 3.8. All subsequent steps have explicit witnesses: orthonormal sequences, a unitary extension when both defects are infinite, and an injective graph construction whose image under the candidate approximant has finite dimension in the finite-cokernel case. The boundary \(\delta<1\) is strict precisely where a Neumann inverse is needed; the norm-one upper bound is attained by zero. The factor \(1/2\) is realized exactly, not only asymptotically.

## Relationship to prior work

Ramesh and Sequeira characterize the norm closure of absolutely norm-attaining operators and show that a partial isometry lies in that closure precisely when it is absolutely norm attaining (Corollary 3.9). Their structural theorem gives a necessary ingredient for the present quantitative comparison, but their membership classification alone yields neither the intermediate distance \(1/2\) nor the dichotomy according to cokernel dimension. In particular, they show that membership in the closure is determined by the modulus, whereas the two examples above show that *distance* to that closure is not. This statement should not be mistaken for a claim that the general distance-to-closure problem for arbitrary operators has been solved.

## Limitations

The classification is restricted to partial isometries on separable infinite-dimensional complex Hilbert space, not arbitrary bounded operators or general Banach spaces. The argument for the intermediate case invokes the published structural theorem rather than reproving it. Related recent work characterizing compact and Schatten-class perturbations of partial isometries could not be fully inspected, so a residual risk of an equivalent formulation remains. No independent audit is claimed.

## References

1. G. Ramesh and S. S. Sequeira, *On the Closure of Absolutely Norm Attaining Operators*, arXiv:2204.05912v1 (first public version, 12 April 2022), especially Theorem 3.7 and Corollaries 3.8–3.9. https://arxiv.org/html/2204.05912v1
2. N. Bala and R. Golla, *Spectral Characterizations of Schatten-class Perturbations of Partial Isometries*, arXiv:2607.15222 (2026; abstract consulted, full-text comparison unresolved). https://arxiv.org/abs/2607.15222
