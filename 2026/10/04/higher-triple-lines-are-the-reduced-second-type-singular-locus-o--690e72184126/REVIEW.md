# Same-model scientific review

## Correctness
PASS. The claim is restricted to the reduced, set-theoretic singular locus. The proof uses the published \(55\)-component decomposition of the Fermat second-type locus, identifies component overlap by coordinate-support degeneration, and compares this to Zhang's higher-triple criterion through a block decomposition of the second fundamental forms. The critical Fermat Hessian identities for block sizes \(3\) and \(4\) are symbolically replayed in `artifacts/verify_fermat_htl.py`. The \(180\)-curve and \(405\)-point incidence counts are exhaustively enumerated by the same script.

Risk retained: the proof does not determine the scheme-theoretic structure or local analytic type of the singular locus, and it does not use the finite enumeration as a replacement for the geometric block-Hessian argument.

## Originality
PASS. Y. Zhang's arXiv:2501.01682 defines higher triple lines, gives the Eckardt/Hessian description, records at least \(45\) one-parameter families for the Fermat cubic fourfold, and asks for the relationship between higher triple lines and singularities of \(F_2\) in dimension at least four. F. Gounelas and A. Kouvidakis, arXiv:2302.09562 / NYJM 31 (2025), determine the \(55\) irreducible components of the Fermat second-type locus and state that it is singular and non-normal, but the inspected text does not identify its singular locus with higher triple lines or state the \(180\)-curve/\(405\)-point incidence structure. Searches for equivalent formulations and the exact numerical pattern in published-finding corpus and on the public web found no covering result.

Residual risk: an equivalent result could exist under different terminology. The abstract of arXiv:2608.08909 was checked because it concerns second-type loci, but its full text was not available through the retrieval path used; its advertised scope is the universal cover of the general second-type locus rather than the special Fermat singular locus.

## Value
PASS. The finding gives a complete answer for the canonical Fermat cubic fourfold to an explicit recent question about higher triple lines versus singularities of the second-type locus. It also sharpens the previously recorded lower bound of \(45\) one-parameter families to an exact \(180\)-component description with a natural \(405\)-point incidence stratum. The statement is structural rather than a routine numerical recomputation: it identifies two independently defined geometric loci and explains their full component incidence in a standard highly symmetric example.

## Closest literature and limitations
Closest sources are Zhang, arXiv:2501.01682, and Gounelas--Kouvidakis, arXiv:2302.09562 / NYJM 31 (2025). The result is deliberately limited to the reduced set-theoretic locus over \(\mathbf C\); nonreduced structure, local multiplicities, and branch transversality remain outside the claim.

Same-model review: passed. Independent audit: not yet performed.
