# Sumset growth from the first Kunz layer at prime multiplicity

## Statement

Let \(S\subseteq\mathbb N\) be a numerical semigroup of multiplicity \(m\). Write its Apéry set with respect to \(m\) as
\[
\operatorname{Ap}(S,m)=\{w_0,\dots,w_{m-1}\},\qquad
w_i=i+m x_i,
\]
where \(w_0=0\) and \(x_i\ge1\) for \(1\le i<m\). Put
\[
A=\{i\in\{1,\dots,m-1\}:x_i=1\},\qquad
X=\{0\}\cup A\subseteq \mathbb Z/m\mathbb Z,
\]
and
\[
\Theta_t=\#\{1\le i<m:x_i\le t\},\qquad \eta=\Theta_1=|A|.
\]

### Theorem 1 (sumset propagation)

For every integer \(h\ge1\),
\[
hX\subseteq \{0\}\cup\{i\in\mathbb Z/m\mathbb Z:x_i\le 2h-1\}.
\]
Consequently
\[
\boxed{\Theta_{2h-1}\ge |hX|-1.}
\]

If \(m=p\) is prime, the Cauchy--Davenport theorem gives the explicit bound
\[
\boxed{\Theta_{2h-1}\ge B_h:=\min\{p-1,h\eta\}.}
\]

Thus, at prime multiplicity, the population of the first Kunz layer forces deterministic growth of higher cumulative Kunz layers.

### Theorem 2 (prime-multiplicity layered Wilf bound)

Assume now that \(m=p\) is prime. Write
\[
c=qp-\rho,\qquad 0\le\rho<p,
\]
let \(e\) be the embedding dimension, \(L=S\cap[0,c)\), and let \(W(S)=e|L|-c\).

For every integer \(k\ge1\) with \(2k+1\le q\),
\[
\boxed{
|L|\ge
q+2\sum_{h=1}^{k-1}B_h+(q-2k)B_k
}
\]
and hence
\[
\boxed{
W(S)\ge
e\left(q+2\sum_{h=1}^{k-1}B_h+(q-2k)B_k\right)-qp+\rho .
}
\]

In particular, any \(k\) satisfying \(2k+1\le q\) certifies Wilf's conjecture whenever
\[
e\left(q+2\sum_{h=1}^{k-1}B_h+(q-2k)B_k\right)+\rho\ge qp.
\]

The lower bound is monotone nondecreasing as \(k\) is increased through its admissible range, so the strongest member obtained this way is at
\[
H=\left\lfloor\frac{q-1}{2}\right\rfloor.
\]

Since \(e\ge\eta+1\), the same statement yields an \((p,q,\rho,\eta)\)-only sufficient criterion by replacing \(e\) with \(\eta+1\).

## Proof

### Proof of Theorem 1

For each residue \(a\in X\), choose an element \(s_a\in S\) by
\[
s_0=m,\qquad s_a=m+a\quad(a\in A).
\]
The second formula is valid because \(x_a=1\) means precisely that the Apéry representative is \(w_a=m+a\).

Take any \(r\in hX\). Choose representatives \(a_1,\dots,a_h\in X\cap\{0,\dots,m-1\}\) whose sum is congruent to \(r\) modulo \(m\). Write
\[
a_1+\cdots+a_h=tm+r,\qquad 0\le r<m.
\]
Because every \(a_j\le m-1\), we have \(0\le t\le h-1\). Adding the corresponding elements of \(S\),
\[
s_{a_1}+\cdots+s_{a_h}
=hm+(a_1+\cdots+a_h)
=(h+t)m+r\in S.
\]
If \(r\ne0\), the Apéry representative \(w_r\) is the least element of \(S\) in residue class \(r\), hence
\[
w_r\le(h+t)m+r,
\]
so
\[
x_r\le h+t\le2h-1.
\]
This proves the containment, and therefore
\[
\Theta_{2h-1}\ge |hX|-1.
\]

When \(m=p\) is prime, repeated Cauchy--Davenport gives
\[
|hX|\ge \min\{p,h|X|-(h-1)\}
=\min\{p,h\eta+1\},
\]
because \(|X|=\eta+1\). Subtracting one yields
\[
\Theta_{2h-1}\ge\min\{p-1,h\eta\}=B_h.
\]
This proves Theorem 1.

### Proof of Theorem 2

The exact cumulative-layer identity
\[
|L|=q+\sum_{t=1}^{q-2}\Theta_t+\Theta_{q-1,\rho},
\]
where the final trimmed term is nonnegative, follows by counting each Apéry residue below the conductor. Hence
\[
|L|\ge q+\sum_{t=1}^{q-2}\Theta_t.
\]

Fix \(k\) with \(2k+1\le q\). For \(1\le h<k\), monotonicity of \(\Theta_t\) and Theorem 1 give
\[
\Theta_{2h-1},\Theta_{2h}\ge B_h.
\]
For every
\[
2k-1\le t\le q-2
\]
we likewise have \(\Theta_t\ge B_k\). There are \(q-2k\) indices in this final range. Therefore
\[
\sum_{t=1}^{q-2}\Theta_t
\ge
2\sum_{h=1}^{k-1}B_h+(q-2k)B_k,
\]
which proves the asserted lower bound for \(|L|\). Since \(c=qp-\rho\),
\[
W(S)=e|L|-c
\]
immediately gives the displayed Wilf bound.

To see monotonicity in \(k\), let \(R_k\) denote the part after \(q\) in the lower bound. Whenever \(k+1\) is admissible,
\[
R_{k+1}-R_k
=(q-2k-2)(B_{k+1}-B_k)\ge0,
\]
because \(B_h\) is nondecreasing and admissibility gives \(q-2k-2\ge1\).

## A concrete semigroup missed by the first-layer criterion

Consider
\[
S=\langle29,41,42,54,56,57\rangle.
\]
Direct Apéry computation gives
\[
m=29,\quad e=6,\quad c=218,\quad q=8,\quad \rho=14,
\]
\[
\eta=5,\qquad
(\Theta_1,\dots,\Theta_6)=(5,7,13,16,21,24),
\]
and
\[
|L|=107,\qquad W(S)=424.
\]

The mixed first-layer criterion of Yang--Zhang,
\[
e(\eta+2)\ge2m,
\]
does not certify this semigroup, since
\[
6(5+2)=42<58.
\]
Their \(\eta\)-only criterion also fails:
\[
(\eta+1)(\eta+2)=42<58.
\]

The prime-multiplicity sumset bound instead gives, at \(H=3\),
\[
(B_1,B_2,B_3)=(5,10,15)
\]
and therefore
\[
|L|\ge8+2(5+10)+2(15)=68.
\]
Consequently
\[
6\cdot68-218=190>0,
\]
already certifying Wilf. This example also has \(c>3m\), \(e<m/3\), nondivisible conductor, and genus \(111\), so it lies outside the four broad numerical regimes highlighted in the 2026 first-layer paper and beyond the published exhaustive genus-\(100\) verification. This is only an illustration of the criterion, not a claim that this individual semigroup was previously unresolved by every known specialized theorem.

## Context and relation to prior work

Yang and Zhang (2026) introduced the first-layer population \(\eta\), derived the exact cumulative-layer formula above, and obtained first-layer and multi-layer sufficient criteria for Wilf's conjecture. Their concluding remarks specifically point to interactions among low Kunz layers as a direction for stronger estimates. The present result supplies one such interaction: additive growth of the residue set \(X=\{0\}\cup\{x_i=1\}\) forces population growth in the odd cumulative layers.

Cauchy--Davenport is classical; no novelty is claimed for the additive-combinatorial theorem itself. Likewise, sumsets and additive-combinatorial constructions have appeared before in work on Wilf's conjecture, notably Eliahou's Macaulay-based argument and Eliahou--Fromentin's \(B_h\)-set constructions. The new claim is the specific sumset-to-Kunz-layer propagation inequality and its prime-multiplicity Wilf consequences above.

## Reproducibility

`artifacts/verify.py` independently computes the Apéry set of the displayed semigroup by shortest paths modulo \(29\), derives its Kunz coordinates and invariants, checks the cumulative layers and the new lower bound, and confirms that the two Yang--Zhang first-layer tests displayed above fail while the new sufficient inequality succeeds.

## Limitations

- The explicit Cauchy--Davenport lower bound \(B_h=\min(p-1,h\eta)\) requires prime multiplicity. The general containment \(\Theta_{2h-1}\ge|hX|-1\) holds for arbitrary multiplicity, but composite moduli can have subgroup obstructions to linear sumset growth.
- The Wilf bound is sufficient, not necessary, and discards the nonnegative trimmed term \(\Theta_{q-1,\rho}\); it is therefore not generally sharp.
- The result does not resolve Wilf's conjecture in full.
- Originality is asserted only to the best of our knowledge. The closest 2026 paper is a recent, non-peer-reviewed preprint, so very recent or incompletely indexed follow-up work remains a residual risk.

## References

1. Y. Yang and Y. Zhang, *Wilf's Conjecture from the First Kunz Layer*, Preprints.org (2026), DOI: 10.20944/preprints202604.0551.v1. https://www.preprints.org/manuscript/202604.0551
2. H. Davenport, *On the Addition of Residue Classes*, J. London Math. Soc. s1-10 (1935), 30--32. DOI: 10.1112/jlms/s1-10.37.30.
3. S. Eliahou, *Wilf's conjecture and Macaulay's theorem*, J. Eur. Math. Soc. 20 (2018), 2105--2129. DOI: 10.4171/JEMS/807.
4. S. Eliahou and J. Fromentin, *Near-misses in Wilf's conjecture*, Semigroup Forum 98 (2019). DOI: 10.1007/s00233-018-9926-5; arXiv:1710.03623.
5. W. Bruns, P. A. García-Sánchez, C. O'Neill, and D. Wilburne, *Wilf's conjecture in fixed multiplicity*, Int. J. Algebra Comput. 30 (2020), 861--882. DOI: 10.1142/S021819672050023X; arXiv:1903.04342.
6. M. Delgado, S. Eliahou, and J. Fromentin, *A verification of Wilf's conjecture up to genus 100*, J. Algebra 664 (2025), 150--163; arXiv:2310.07742.
