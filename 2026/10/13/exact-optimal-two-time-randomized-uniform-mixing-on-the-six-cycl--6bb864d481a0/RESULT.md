# Exact optimal two-time randomized uniform mixing on the six-cycle

## Finding

The unweighted six-cycle admits **exact uniform mixing in expectation under a probability law with exactly two observation times, and no one-time law works**. With the notation below, the explicit identity is
\[
w_-M(t_-)+w_+M(t_+)=J_6/6.
\]
For every real cutoff \(T\ge0\), both observation times can be chosen strictly greater than \(T\) while retaining the same weights and mixing matrix.

## Assumptions and scope

Let \(C_6\) be the simple undirected cycle with vertex set \(\mathbb Z/6\mathbb Z\) and an edge between residues differing by one. Let \(A\) be its unweighted adjacency matrix, \(U(t)=e^{itA}\), and \(M(t)_{uv}=|U(t)_{uv}|^2\). Observation-time laws are arbitrary finite-support probability measures on nonnegative real times; the same law must work simultaneously for every initial vertex. Uniform mixing means that the expected transition matrix equals \(J_6/6\), not merely that one row is approximately flat.

Define
\[
c_-=\frac{2-\sqrt6-\sqrt{10}}4,\quad c_+=\frac{2-\sqrt6+\sqrt{10}}4,
\]
\[
w_-=\frac12+\frac{4\sqrt{10}-3\sqrt{15}}{50},\quad w_+=1-w_-,\qquad t_\pm=\arccos(c_\pm).
\]
Both cosine values lie strictly between \(-1\) and \(1\); both probabilities lie strictly between \(0\) and \(1\); and \(c_-\ne c_+\). The principal inverse cosine makes both times positive and distinct.

## Proof

**Exact transition classes.** Translation and reflection symmetry imply that \(M(t)\) depends only on cycle distance \(d=0,1,2,3\). Since the adjacency eigenvalues are \(2,1,1,-1,-1,-2\), Fourier inversion gives, for any two vertices separated by \(d\) edges,
\[
U_d(t)=\frac16\left(e^{2it}+(-1)^d e^{-2it}+2\cos(\pi d/3)e^{it}+2\cos(2\pi d/3)e^{-it}\right).
\]
Putting \(c=\cos t\), taking absolute squares and simplifying gives precisely
\[
\begin{aligned}
p_0(c)&=(2c^2+2c-1)^2/9,\\
p_1(c)&=(1-c^2)(2c+1)^2/9,\\
p_2(c)&=(1-c)^2(2c+1)^2/9,\\
p_3(c)&=4(1-c)^3(1+c)/9.
\end{aligned}
\]
The unitary normalization is \(p_0(c)+2p_1(c)+2p_2(c)+p_3(c)=1\) for every \(c\in[-1,1]\).

**Explicit two-point uniformity.** Direct radical simplification, for each \(d\in\{0,1,2,3\}\), yields
\[
w_-p_d(c_-)+w_+p_d(c_+)=\frac16.
\]
The displayed radical formulas and the four explicit polynomials make these four exact algebraic identities independently checkable; `verify_c6.py` verifies each in symbolic algebra rather than numerically. Since every matrix entry belongs to one of the four distance classes, the four identities prove the six-by-six matrix assertion.

**Optimality.** If one observation time yielded uniform mixing, then both distance-one and distance-two probabilities would be \(1/6\). But
\[
p_1(c)-p_2(c)=\frac{2c(1-c)(2c+1)^2}{9}.
\]
Thus equality requires \(c\in\{0,1,-1/2\}\). At these three values, respectively, \(p_1(c)\) equals \(1/9,0,0\), never \(1/6\). A probability law with just one support point is impossible, so two is the exact minimum.

**Arbitrarily late times.** The six-cycle has integral adjacency eigenvalues, so \(U(t+2\pi k)=U(t)\) for every integer \(k\). For any \(T\ge0\), choose an integer \(k\) sufficiently large that \(t_-+2\pi k>T\) and \(t_++2\pi k>T\). Shifting both times by \(2\pi k\) leaves the mixing identity unchanged. No limiting approximation is used.

## Verification

Run `python verify_c6.py` with Python, SymPy, NumPy, and SciPy installed. The checker reproduces the transition-class normalization, verifies all four exact weighted probability identities, checks the exhaustive three-case one-time obstruction, and independently forms six-by-six matrix exponentials with a numerical residual below \(10^{-13}\). The symbolic identities and the preceding proof, not the floating-point check, establish the exact theorem.

## Relationship to prior work

Baptista, Coutinho and Marques [1] introduced observation-time distributions other than the usual long-time Cesàro distribution and exhibited exact uniform expected mixing for short paths. Their inspected arXiv preprint treats paths on three and four vertices but does not state this explicit two-atom six-cycle result. Adamczak et al. [2] proved non-uniformity for standard cycle mixing conventions; their Cesàro-average obstruction has different sampling quantifiers and therefore does not cover arbitrary two-point time laws. The spectral framework of Coutinho et al. [3] and the usual projector-based average mixing matrix of Coutinho et al. [4] concern different time-weighting regimes. The distinguishing assertion here is the explicit exact law together with a matching minimal-support lower bound.

## Limitations

The claim concerns exactly the unweighted six-cycle under adjacency-generated continuous-time evolution and classical randomization of observation time. It gives no claim for other cycles, no noise robustness or hardware implementation guarantee, and no classification of all possible two-point laws. The exact algebra is fully verified; originality is subject to the ordinary risk of an unlocated equivalent formulation in the extensive quantum-walk literature. A search absence alone is not asserted as a proof of novelty.

## References

[1] P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378 (initial submission 2023-08-31). https://arxiv.org/abs/2308.16378

[2] W. Adamczak et al., *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096 (2007). https://arxiv.org/abs/0708.2096

[3] G. Coutinho et al., *Irrational quantum walks*, arXiv:2208.08971 (2022). https://arxiv.org/abs/2208.08971

[4] G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (2017). https://arxiv.org/abs/1709.03591
