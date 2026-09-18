# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The central equivalence is immediate from the definitions but was checked in both directions. If \(\operatorname{Inv}(A)=\operatorname{Inv}_0(A)\), the membership tests defining ordinary and exponential spectra coincide. Conversely, if \(\varepsilon_A(a)=\sigma_A(a)\) for every \(a\), then for an arbitrary invertible \(u\), taking \(a=1-u\) gives \(1\notin\sigma_A(a)\), hence \(1\notin\varepsilon_A(a)\), so \(u\in\operatorname{Inv}_0(A)\). Thus the invertible group is connected.

For \(A=\mathcal B(X)\), this identifies the structural condition with connectedness of \(\operatorname{GL}(X)\). Ordinary Jacobson spectral commutativity away from zero then transfers verbatim to exponential spectrum.

The classical-space input was checked against de Rancourt's explicit introduction: it lists connectedness of the general linear groups of \(c_0\), \(\ell_p\) for \(1\le p<\infty\), \(C[0,1]\), \(L_1[0,1]\), \(L_\infty[0,1]\), \(\ell_\infty\), and \(L_p[0,1]\) for \(1<p<\infty\). The same source states connectedness for every complex HI space. Mityagin's 1970 survey independently corroborates the classical \(c_0\), \(\ell_p\), and Hilbert-space contractibility facts.

The modern extension was checked against the bibliographic record and seminar abstract for Pliev--Sukochev--Tomskova, which state contractibility for the specified Lebesgue--Bochner, vector-valued sequence, and Besov spaces.

The sharpness discussion distinguishes pointwise collapse from mere commutativity. Daniel--Ghosh's published abstract states commutativity for \(\mathcal B(\ell^p\oplus\ell^q)\), while de Rancourt records Douady's disconnectedness result for direct sums of distinct members of the \(\ell_p/c_0\) family. No claim is made that connectedness is necessary for commutativity.

## Originality

Horváth--Kania v1 was inspected at its definitions, stable-rank discussion, Section 7 component criterion, and Section 9. Question 9.2 explicitly asks whether exponential-spectral commutativity can fail on a classical sequence or function space and which structural properties exclude failure. Searches in the full text found no occurrence of Mityagin, Pliev, "contractible", or "general linear group".

The implication "connected invertible group implies exponential spectrum equals ordinary spectrum" is not new. A 2009 MathOverflow discussion explicitly records it, and it is also immediate from the definitions. The converse is equally elementary. The review therefore assigns no originality to the abstract criterion itself.

The originality claim is instead the literature-grounded application to the newly posed 2026 question: combining the classical and recent homotopy results gives an immediate but apparently unrecorded no-twisting theorem covering the standard \(c_0\), \(\ell_p\), \(C[0,1]\), and \(L_p[0,1]\) families and several newer Bochner/Besov classes. Searches for exact and synonymous formulations using "exponential spectrum", "connected/contractible general linear group", the named classical spaces, Horváth--Kania, Mityagin, and Pliev did not locate an existing publication making this connection.

Originality status: pass, to the best of our knowledge, specifically for this application and synthesis rather than for the elementary component observation.

## Value

The result gives a direct structural answer to a current explicit open question and removes its most canonical sequence- and function-space cases. It also identifies an exact boundary for the stronger property \(\varepsilon(T)=\sigma(T)\) for all operators.

The Hilbert-space comparison is informative: Horváth--Kania record \(\operatorname{tsr}\mathcal B(H)=\infty\), while the general linear group is contractible. Thus infinite stable rank can coexist with complete exponential-spectrum collapse, separating two topological mechanisms that might otherwise be conflated.

The mixed \(\ell_p\oplus\ell_q\) comparison shows that disconnectedness does not itself produce twisting, so the criterion is sharp as a characterization of pointwise collapse but deliberately not advertised as a characterization of commutativity.

## Scientific limitations

- The phrase "classical sequence or function space" is broader than a fixed formal list. The result rules out failure on the standard canonical families stated above but does not claim to settle Question 9.2 in full.
- The connectedness criterion is elementary and its forward direction was explicitly known by 2009; only the 2026 application is claimed as new to the best of our knowledge.
- The Daniel--Ghosh full article was not inspected; only its published abstract and Horváth--Kania's theorem-level description were used.
- For the Pliev--Sukochev--Tomskova extension, the bibliographic record and a detailed author seminar abstract were inspected, not the complete journal text.
- Some original 1960s--1970s connectedness papers were not individually reread. De Rancourt's article was used as the explicit modern source summarizing those classical results, with Mityagin independently corroborating several central cases.
- An older exponential-spectrum source may have combined these homotopy facts under different terminology and escaped the searches.
