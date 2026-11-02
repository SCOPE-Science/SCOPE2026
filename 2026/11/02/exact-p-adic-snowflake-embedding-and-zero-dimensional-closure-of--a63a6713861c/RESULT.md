# Exact p-adic snowflake embedding and zero-dimensional closure of Pascal-row integers

## Finding
Fix any prime \(p\). The integer obtained by reading row \(n\) of Pascal's triangle modulo \(p\) as a base-\(p\) integer is
\[
t_p(n)=\sum_{i=0}^{n}\left[\binom{n}{i}\right]_p p^i,\qquad n\in\mathbb N_0,
\]
where \([a]_p\) denotes the unique integer in \(\{0,\ldots,p-1\}\) congruent to \(a\) modulo \(p\).

**Theorem.** For distinct nonnegative integers \(m,n\),
\[
\nu_p\bigl(t_p(m)-t_p(n)\bigr)=p^{\nu_p(m-n)}. \tag{1}
\]
There is a unique continuous extension \(T_p:\mathbb Z_p\to\mathbb Z_p\), and (1) holds for every distinct \(x,y\in\mathbb Z_p\) in place of \(m,n\). It is a homeomorphism onto the closure \(E_p\) of the original row integers.

Writing \(x=\sum_{j\ge0}x_jp^j\) and \(i=\sum_{j\ge0}i_jp^j\) with standard base-\(p\) digits, define
\[
d_i(x)=\left[\prod_{j\ge0}\binom{x_j}{i_j}\right]_p.\tag{2}
\]
(The product is finite because all but finitely many \(i_j\) vanish.) Then
\[
T_p(x)=\sum_{i\ge0} d_i(x)p^i,\qquad d_{p^j}(x)=x_j.\tag{3}
\]
The closed image consists **exactly** of those \(p\)-adic integers with digits \(z_i\) satisfying \(z_0=1\) and
\[
z_i=\left[\prod_{j\ge0}\binom{z_{p^j}}{i_j}\right]_p\quad(i\ge1).\tag{4}
\]
For every integer \(N\ge1\), put \(J_p(N)=\min\{j\in\mathbb N_0:p^j\ge N\}\). The number of attained residue classes modulo \(p^N\) is **exactly**
\[
\bigl|E_p\bmod p^N\bigr|=p^{J_p(N)}.\tag{5}
\]
The natural pushforward of normalized Haar measure on \(\mathbb Z_p\) gives each attained class probability \(p^{-J_p(N)}\) and every unattained class probability zero. The compact set \(E_p\) is uncountable, perfect, nowhere dense and Haar-null, with Hausdorff dimension zero and both upper and lower box dimensions zero for the standard \(p\)-adic metric.

## Assumptions and scope
The theorem holds **for each prime** \(p\), all \(m,n\in\mathbb N_0\) with \(m\ne n\), all \(x,y\in\mathbb Z_p\) with \(x\ne y\), and all integer precisions \(N\ge1\). All digits are least nonnegative residues; trailing zeros are included in the infinite \(p\)-adic expansion. We use \(\nu_p(0)=+\infty\). The relevant dimension is that of the one-dimensional image in \(\mathbb Z_p\), **not** that of the planar Sierpiński-type Pascal triangle.

## Proof
**Step 1 — Lucas digits.** Lucas's theorem gives, for nonnegative integers \(n=\sum n_jp^j\) and \(i=\sum i_jp^j\),
\[
\left[\binom ni\right]_p=\left[\prod_j\binom{n_j}{i_j}\right]_p,
\]
with \(\binom ab=0\) for \(b>a\). The coefficient is zero when \(i>n\), so this holds at **every** digit position \(i\ge0\) in the infinite expansion of \(t_p(n)\). In particular, at index \(i=p^j\) the digit is \(n_j\).

**Step 2 — first mismatch.** If \(m\ne n\) and \(j=\nu_p(m-n)\), their first \(j\) input digits agree and the input digits in position \(j\) disagree. Every output index \(i<p^j\) has zero base-\(p\) digits above position \(j-1\), so Lucas's formula makes its output digit the same for both inputs. At output index \(i=p^j\), the two output digits are respectively \(m_j\) and \(n_j\), which differ in \(\{0,\ldots,p-1\}\). Hence the first nonzero digit in the difference of the integer outputs occurs at precisely position \(p^j\), proving (1) including the leading digit boundary \(j=0\).

**Step 3 — extension and inverse.** For each output precision \(N\ge1\), all output digits with indices \(i<N\) depend only on the \(J_p(N)\) input digits \(x_0,\ldots,x_{J_p(N)-1}\). Therefore the digit formula (2) is well-defined on all \(x\in\mathbb Z_p\) and is continuous. It extends the original integer map. Density of \(\mathbb N_0\) in \(\mathbb Z_p\) ensures uniqueness and that the compact image is exactly its closure. The mismatch argument of Step 2 remains valid for any two distinct \(p\)-adic inputs and yields the valuation identity. Thus the map is injective and a homeomorphism of the compact \(\mathbb Z_p\) onto its Hausdorff image. Formula (3) recovers each input digit directly from output position \(p^j\). Therefore (4) is necessary; it is sufficient by choosing \(x_j=z_{p^j}\), after which (2) reproduces every output digit of \(z\).

**Step 4 — exact finite spectra and measure.** Modulo \(p^N\), only the first \(J_p(N)\) input digits can affect the output, hence there are **at most** \(p^{J_p(N)}\) distinct values. Conversely, for each \(0\le j<J_p(N)\) one has \(p^j<N\), and the output at digit index \(p^j\) exactly records \(x_j\). Distinct choices of these input digits thus yield **distinct** outputs modulo \(p^N\), proving (5). For uniformly distributed input in \(\mathbb Z_p\), each input prefix has Haar probability \(p^{-J_p(N)}\). Every attained output residue has exactly one such prefix, proving uniform cylinder weights.

**Step 5 — fractal conclusions.** At precision \(N\), the image lies in \(p^{J_p(N)}\) balls of radius \(p^{-N}\). Since \(p^{J_p(N)}\le pN\), for every real \(s>0\) the sum of \(s\)-powers of the radii is bounded by \(pN p^{-sN}\to0\). Thus the Hausdorff dimension is zero. The exact cylinder count gives box dimension \(\lim_{N\to\infty}\log(p^{J_p(N)})/\log(p^N)=0\). The Haar measure is the limit of \(p^{J_p(N)-N}=0\) as \(N\to\infty\). The image is compact and hence closed, has empty interior because each nonempty open ball has positive Haar measure, and is perfect because \(\mathbb Z_p\) is perfect and \(T_p\) is a homeomorphism. It is uncountable because its source is uncountable. This completes the proof.

## Verification
The included standard-library Python checker `verify_pascal_closure.py` independently constructs actual row integers using exact binomial coefficients and checks the first-mismatch valuation identity for every ordered distinct pair drawn from indices \(0\) through \(80\), for \(p\in\{2,3,5,7\}\). It also compares independent Lucas-digit computations with those exact integer outputs, and exhaustively verifies the finite residue count and coordinate decoding for \(p\in\{2,3,5\}\), precisions \(1\le N\le14\). Observed totals: 12,960 valuation checks, 9,800 digit checks, 42 finite-residue cases, all passed. Finite computation does not establish the infinite theorem, which is proved above.

## Relationship to prior work
Mathonet, Rigo, Stipulanti and Zénaïdi defined exactly this integer sequence and developed its base-\(p\) digit recursions, multiplicative structure, and links with Fermat/Roberts numbers and automatic sequences. Their 2022 open preprint supplies the underlying Lucas-congruence identities; those are **not** claimed to be new. The result here instead identifies the **exact distance distortion for all pairs**, gives a complete description of the \(p\)-adic closure and inverse, counts every finite-level residue fiber, and determines the resulting dimension and distribution. Those statements were not located in that inspected preprint or the two pertinent OEIS entries. The older Pascal-fractal literature concerns rescaled two-dimensional divisibility patterns and cannot be equated to this one-dimensional \(p\)-adic image merely because both invoke Lucas's theorem.

## Limitations
This is a theorem about the canonical **least-residue integer encoding** of Pascal rows. It does not classify arbitrary polynomial evaluations of Pascal rows, congruences modulo \(p^r\) before digit conversion, or the dimensions of planar Pascal triangle fractals. The 1992 primary article by von Haeseler, Peitgen and Skordev was only accessible through its abstract/references for this comparison, leaving a nonzero risk of unlocated implicit prior coverage. No independent scientific audit has been performed.

## References
1. P. Mathonet, M. Rigo, M. Stipulanti, N. Zénaïdi, *On digital sequences associated with Pascal's triangle*, first public arXiv version 17 January 2022, arXiv:2201.06636v1, https://arxiv.org/pdf/2201.06636, later Aequationes Mathematicae, DOI:10.1007/s00010-022-00932-z.
2. É. Lucas, *Théorie des fonctions numériques simplement périodiques*, American Journal of Mathematics 1 (1878), 184–240, 289–321; Lucas binomial congruence, as reproduced in Theorem 1 of reference 1.
3. OEIS A001317, https://oeis.org/A001317 (binary Roberts/Pascal-row integers), and OEIS A173019, https://oeis.org/A173019 (ternary Pascal-row integers).
4. F. von Haeseler, H.-O. Peitgen, G. Skordev, *Pascal's triangle, dynamical systems and attractors*, Ergodic Theory and Dynamical Systems 12 (1992), 479–486, DOI:10.1017/S0143385700006908 (abstract and bibliographic record inspected; full text not obtained).
