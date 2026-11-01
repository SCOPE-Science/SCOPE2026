# The first two integer Fourier levels of the uniform Sierpiński carpet measure

## Finding

Let \(\mu\) be the uniform eight-map probability measure on the standard planar Sierpiński carpet, with its support affinely normalized to \([0,1]^2\) and considered as a measure on \(\mathbb T^2\). For nonzero integer pairs \((m,n)\), the largest and second-largest distinct values of \(|\widehat\mu(m,n)|\) are exactly
\[
A=\frac18\prod_{j=2}^{\infty}\frac{1+3\cos(2\pi/3^j)}4
 =0.100726872473424\ldots,
\qquad
B=\frac18\prod_{j=2}^{\infty}\frac{(1+2\cos(2\pi/3^j))^2-1}8
 =0.080754932274794\ldots.
\]
The value \(A\) is attained **only** at \((m,n)=3^r(\pm1,0)\) and \((m,n)=3^r(0,\pm1)\), where \(r\ge0\). The value \(B\) is attained **only** at \((m,n)=3^r(\pm1,\pm1)\), where both signs may be selected independently and \(r\ge0\). Every other nonzero integer Fourier coefficient has modulus strictly less than \(B\). More quantitatively, if exactly one coordinate of the reduced frequency is divisible by three and the reduced frequency is not an extremizing axis vector, then the modulus is at most \(1/16<B\).

Every integer Fourier coefficient \(\widehat\mu(m,n)\), including those away from these extremal families, is nonzero. Consequently convolution by \(\mu\) on the mean-zero subspace of \(L^2(\mathbb T^2)\) has sharp operator norm \(A\). On the orthogonal complement of all axis extremizing characters within that subspace, its sharp norm is \(B\); the norms of its positive integer powers are respectively \(A^r\) and \(B^r\). Convolution by \(\mu\) is injective on \(L^2(\mathbb T^2)\).

## Assumptions and scope

The digit set is \(\mathcal D=\{0,1,2\}^2\setminus\{(1,1)\}\), with its eight points uniformly weighted. Let \(U_1,U_2,\ldots\) be independent uniform \(\mathcal D\)-valued random vectors and set \(X=\sum_{j=1}^{\infty}3^{-j}U_j\). The probability law \(\mu\) of \(X\) on \([0,1]^2\), reduced modulo integers on \(\mathbb T^2\), is the measure under study. We normalize \(\widehat\mu(m,n)=\int e^{-2\pi i(mx+ny)}\,d\mu(x,y)\) for \((m,n)\in\mathbb Z^2\). The displayed constants are exact convergent infinite products; decimal values are supplementary. All extremizer and strict-inequality statements quantify over all nonzero integer pairs, not merely bounded boxes.

## Proof

**1. The product and its three-adic reduction.** Put \(s(t)=1+2\cos(2\pi t)\). Summing over the nine possible digit pairs and subtracting the omitted center gives the exact mask identity
\[
M(x,y)=\frac18\sum_{(a,b)\in\mathcal D}e^{-2\pi i(ax+by)}
=e^{-2\pi i(x+y)}\frac{s(x)s(y)-1}{8}.
\]
Independence and absolute convergence of the digit expansion give \(\widehat\mu(m,n)=\prod_{j=1}^{\infty}M(m/3^j,n/3^j)\). Inserting an initial zero fractional argument shows \(\widehat\mu(3m,3n)=\widehat\mu(m,n)\). We may therefore remove all common powers of three from a nonzero frequency and assume that at least one of \(m,n\) is not divisible by three. For every such reduced pair, \(s(m/3)s(n/3)=0\), hence \(|M(m/3,n/3)|=1/8\).

**2. The pointwise upper bounds.** For \(j\ge2\), set \(a_j=s(3^{-j})\), \(c_j=(3a_j-1)/8\), and \(b_j=(a_j^2-1)/8\). Since \(\cos(2\pi/9)>2/3\), all \(a_j>7/3\); therefore \(c_j>0\), \(b_j>4/8\), and \(c_j>b_j\) (indeed \(c_j-b_j=a_j(3-a_j)/8>0\)). When \(m\) is not divisible by three, \(s(m/3^j)\in[-1,a_j]\), whereas \(s(n/3^j)\in[-1,3]\). If their product is nonnegative its value is at most \(3a_j\); if negative it is at least \(-3\). As \(3a_j-1>4\), this proves \(|M(m/3^j,n/3^j)|\le c_j\). Equality requires that the primitive coordinate be congruent to \(\pm1\) and the other coordinate to \(0\) modulo \(3^j\). If both coordinates are nonzero modulo three, each factor \(s\) lies in \([-1,a_j]\). In this case the product is at most \(a_j^2\) when nonnegative (the product of two negative factors is at most one), and at least \(-3\) otherwise. Since \(a_j^2-1>4\), we obtain \(|M(m/3^j,n/3^j)|\le b_j\), with equality only when each coordinate is congruent to \(\pm1\) modulo \(3^j\).

These bounds are attained simultaneously for all \(j\ge2\) by \((1,0)\) and \((1,1)\), respectively. Applying the equality conditions at all moduli \(3^j\) shows that the only primitive maximizers are the signed axis unit vectors in the first case and the independently signed coordinate-one vectors in the second. Thus the exact first and second candidate products are \(A\) and \(B\), with \(A>B\). The first-level factor was already fixed at \(1/8\).

**3. Uniform suppression of every remaining one-coordinate-primitive frequency.** Consider a reduced pair for which exactly one coordinate is divisible by three; fix the primitive coordinate as the first coordinate. If the pair modulo nine is not an axis unit vector, the second mask has modulus at most \(1/2\): if the divisible coordinate is congruent to \(\pm3\) modulo nine, its \(s\)-factor is zero and the mask modulus is \(1/8\); otherwise that coordinate is zero modulo nine, and the primitive coordinate has residue \(\pm2\) or \(\pm4\). In those latter cases the mask modulus is \(|1+3\cos\theta|/4\le1/2\), since its possible cosines lie between \(-1\) and \(\cos(4\pi/9)=\sin(\pi/18)<1/3\).

If the pair is axis-unit modulo nine but not literally a signed axis-unit integer vector, choose the first \(j\ge3\) at which the axis-unit congruence fails. If the previously zero coordinate first becomes nonzero at this modulus, its residue is \(\pm3^{j-1}\), its \(s\)-factor vanishes, and the mask modulus is \(1/8\). Otherwise the primitive coordinate differs from its signed unit residue by \(\pm3^{j-1}\), so its normalized residue lies in \([1/4,3/4]\); its \(s\)-factor is in \([-1,1]\), and the mask modulus is at most \(1/2\). Thus every nonaxis reduced pair of this kind has at least one mask after the first of modulus at most \(1/2\). All masks have modulus at most one. Hence its entire Fourier modulus is at most \(1/16\).

**4. Ordering the two levels.** As \(c_j>b_j\), \(A>B\). To show \(B>1/16\), use \(\cos(2\pi/9)>2/3\) to get \(b_2>5/9\). For \(j\ge3\), the inequality \(\cos u\ge1-u^2/2\) gives \(b_j\ge1-3(2\pi/3^j)^2/4\). Since every term on the right is positive, \(\prod_{j=3}^{\infty}b_j\ge1-\sum_{j=3}^{\infty}3(2\pi/3^j)^2/4=1-\pi^2/216>103/108\), using \(\pi^2<10\). Consequently
\[
B>\frac18\cdot\frac59\cdot\frac{103}{108}=\frac{515}{7776}>\frac1{16}.
\]
Combining this strict inequality with steps 2 and 3 proves both extremal levels and every equality case. This separation uses a genuine infinite-frequency argument: no enumeration is assumed to exhaust the integer lattice.

**5. There are no Fourier zeros.** For any \(j\ge1\), let \(\zeta=e^{-2\pi i/3^j}\). The unnormalized mask numerator equals \(\zeta^{m+n}(s_j(m)s_j(n)-1)\), where \(s_j(h)=1+\zeta^h+\zeta^{-h}\). In the cyclotomic integer ring \(\mathbb Z[\zeta]\), reduction \(\zeta\mapsto1\) modulo three is a well-defined homomorphism to \(\mathbb F_3\), because \(\Phi_{3^j}(1)=3\). Under this map the parenthetical numerator becomes \(3\cdot3-1\equiv-1\pmod3\), so it is nonzero. Every mask factor is therefore nonzero. For each fixed integer frequency, \(M(m/3^j,n/3^j)=1+O(3^{-j})\) as \(j\to\infty\), making the tail an absolutely convergent product with nonzero limit. Thus \(\widehat\mu(m,n)\ne0\) for all integer pairs.

**6. Operator consequences.** On \(L^2(\mathbb T^2)\), convolution by \(\mu\) acts diagonally on Fourier characters with multipliers \(\widehat\mu(m,n)\). Their absolute values have supremum \(A\) on nonzero frequencies, attained on precisely the first family; after excluding that family the supremum is \(B\), attained on the second. Taking positive integer powers multiplies each Fourier multiplier to that power. Nonvanishing proves injectivity. These assertions do not imply bounded invertibility, since the coefficients need not be bounded away from zero.

## Verification

The accompanying standard-library Python script `artifacts/verify.py` independently reconstructs the digit mask, checks its trigonometric factorization on rational inputs, checks each nine-adic nonaxis residue bound, enumerates the two frequency families and their strict separation over a finite \(85\times85\) frequency box, verifies the rational separation bound, and checks the three-adic cyclotomic reduction certificate. Run `python3 artifacts/verify.py` from the directory containing these files. Its expected line is `CARPET_FOURIER_CERTIFICATE_OK 12306 mask_and_frequency_checks`. The script is supplementary: the proof above establishes the unrestricted infinite-frequency assertions.

## Relationship to prior work

Early Fourier/diffraction discussions explicitly used the Sierpiński carpet as a motivating self-similar geometry (Lakhtakia, Varadan, and Varadan, 1986). Barral and Mensi (2007) developed multifractal theory for self-affine carpet measures. Murugan and Shimizu (2023 preprint; 2025 journal article) study the same standard eight-map uniform carpet probability measure in connection with Sobolev energies. The earlier source's 1986 conference abstract is short and does not state Fourier-coefficient extrema; the accessible Barral–Mensi abstract concerns multifractal dimensions; the examined introduction and stated theorems of Murugan–Shimizu concern energies and Sobolev structure. None of the materially examined statements supplies the first and second sharp integer Fourier levels or the cyclotomic nonvanishing argument. General mask-product methods alone do not establish the global extremizer and equality classifications without the specific inequalities above. Other older Fourier-diffraction literature might nevertheless contain an equivalent result; historical priority is not claimed.

## Limitations

The finding is restricted to the **uniform** eight-map standard planar carpet measure, integer lattice frequencies and the stated affine/torus normalization. It does not classify a third Fourier level, coefficient phases, or analogous extrema for unequal digit weights or other carpets. The analytic proof is independent of finite checks, whose box and precision do not certify unbounded frequencies. The 1986 source was inspected as a conference abstract only, and the complete 2007 article was not accessible for definitive comparison; equivalent results in older fractal harmonic analysis remain a substantive originality risk. Independent external validation has not been performed.

## References

1. A. Lakhtakia, V. K. Varadan, and V. V. Varadan, *Self-Similar Fractals and Fourier Transforms*, abstract in the 1986 National Radio Science Meeting program, scheduled presentation 1986-06-10, p. 150 of the electronic program, https://sites.nationalacademies.org/cs/groups/pgasite/documents/webpage/pga_183543.pdf .
2. J. Barral and M. Mensi, *Gibbs measures on self-affine Sierpiński carpets and their singularity spectrum*, Ergodic Theory and Dynamical Systems 27 (2007), 1419–1443, first published online 2007-10-01, https://doi.org/10.1017/S0143385706001027 .
3. M. Murugan and R. Shimizu, *First-order Sobolev spaces, self-similar energies and energy measures on the Sierpiński carpet*, arXiv:2308.06232, first posted 2023-08-11, https://arxiv.org/abs/2308.06232 ; Communications on Pure and Applied Mathematics, 2025, https://doi.org/10.1002/cpa.22247 .
