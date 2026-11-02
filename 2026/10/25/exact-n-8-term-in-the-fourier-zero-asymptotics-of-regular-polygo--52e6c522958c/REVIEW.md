# Independent mathematical audit

## correctness

PASS

For area-pi regular P_(2n) the sector radial perturbation h=R−1 has uniform expansion h=n^-2 G0+n^-4 G1+O(n^-6). Area equality cancels I1+I2/2 exactly. Independent rational polynomial integrations give I3=pi^7/(15120 n^6)+13 pi^9/(1209600 n^8)+O(n^-10) and I4=pi^9/(120960 n^8)+O(n^-10). Bessel expansion r J1(jr)/j has cubic −j²J0(j)/6 and quartic −j²J0(j)/12, giving Fourier offset at j. Fourier angular harmonics are factorially small, while the cited nearest-zero theorem and derivative at j bound the root shift by O(n^-6) with derivative correction O(n^-4). Division yields j+j³pi^6/(181440 n^6)+j³pi^8/(806400 n^8)+O(n^-10). Independent checks: Independently computed exact SymPy rational integrals of G0³, 3G0²G1 and G0^4 on [-1,1], obtaining 1/15120, 13/1209600, 1/120960; read actual standard-library checker verify_asymptotic.py blob a8211b1a4eb531a180a0ae4d76c4acdbee53007c. Cross-checked Bessel coefficient algebra and relevant precursor paper localization and derivative assumptions. Integral certificate alone would not prove nearest-zero direction or uniform remainder; those depend on cited analytical estimates.

## originality

PASS

Gómez-Serrano–Levitin–Platt–Polterovich arXiv:2609.10517v1 (primary full PDF inspected, Theorem 4.6 near p.20) establishes only j+j³pi^6/(181440 n^6)+O(n^-8), expressly noting apparent genuine next term from numerics. It does NOT give the next coefficient. Same-paper closest stronger result was directly inspected rather than assumed novel by title. Residual limits explicitly listed in originality.residual_risks.

## value

PASS

Exact first nontrivial correction beyond the published leading n^-6 asymptotic for a canonical isoperimetric Fourier-zero functional; determines the previously undetermined n^-8 coefficient and improves the quantified error to O(n^-10) using radial moment cancellation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
